#coding=utf-8
import paramiko
import os,time,sys

class remote_paramiko(object):
    def __init__(self,ip,user,passwd,port=22,**kwargs):
        self.ip = ip
        self.user = user
        self.passwd = passwd
        self.kw = kwargs
        self.port = port
        self.conn = self._conn()
        self.up_down_file_conn = self._up_down_file_conn()
        self._log = sys.stdout.write

    def call_log(self,func):
        """
        日志回调接口

        :param func:
        :return:
        """
        self._log = func

    def _conn(self):
        """
        ssh 初始化链接...
        :return:
        """
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip,self.port,self.user,self.passwd)
        return ssh

    def _up_down_file_conn(self):
        """
        sftp初始化链接...
        :return:
        """
        t = paramiko.Transport((self.ip,self.port))
        t.connect(username=self.user,password=self.passwd)
        sftp = paramiko.SFTPClient.from_transport(t)
        return sftp

    def run(self, shell):
        rs = self._execute(shell=shell)
        return rs

    def _execute(self,shell):
        self._log(u"开始执行命令 -- > %s" % shell)
        stdin, stdout, stderr = self.conn.exec_command(shell)
        rs = stdout.readlines()

        self._log(u"命令执行结果返回:%s" % "".join(rs))

        return rs

    def put_file(self,localfile,remotefile):
        self._log(u"开始上传文件%s --> %s" % (localfile,remotefile))
        self.up_down_file_conn.put(localfile,remotefile)

    def get_file(self,remotefile,localfile):
        self._log(u"开始下载文件%s --> %s" % (remotefile,localfile))
        self.up_down_file_conn.get(remotefile,localfile)

    def execute_close(self):
        try:
            self.conn.close()
            self._log(u"%s对象结束，调用execute_close关闭方法" % self.ip)
        except Exception,e:
            self._log(u"%s已经conn关闭了" % self.ip)

    def sftp_close(self):
        try:
            self.up_down_file_conn.close()
            self._log(u"%s对象结束，调用sftp_close关闭方法" % self.ip)

        except Exception,e:
            self._log(u"%s已经conn关闭了" % self.ip)

    def __del__(self):
        self.execute_close()
        self.sftp_close()

if __name__ == '__main__':
    """使用方法
    t = remote_paramiko("ip","username","passwd")
    t.run("df -TH")
    #投递文件...
    t.put_file("local_file","remote_file")
    #get文件
    t.get_file("remote_file","local_file")
    
    #日志回调钩子函数.
    t.call_log(func)...
    """
    p = remote_paramiko("192.168.0.110","root","111111")
    p.run("df -TH")

