#coding=utf-8
import paramiko
import os,time

class F_bushu(object):
    def __init__(self,ip,user,passwd,port=22,**kwargs):
        self.ip = ip
        self.user = user
        self.passwd = passwd
        self.kw = kwargs
        self.port = port
        self.conn = self._conn()
        self.up_down_file_conn = self._up_down_file_conn()

    def _conn(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(self.ip,self.port,self.user,self.passwd)
        except Exception,e:
            print e
            print u"%s 连接失败." % self.ip
            return False
        return ssh

    def _up_down_file_conn(self):
        try:
            t = paramiko.Transport((self.ip,self.port))
        except Exception,e:
            print e
            print u"%s -> sftp连接失败." % self.ip
            return False
        try:
            t.connect(username=self.user,password=self.passwd)
        except Exception,e:
            print e
            return False
        sftp = paramiko.SFTPClient.from_transport(t)

        return sftp

    def is_conn_sftp(self):
        if not self.conn and not self.up_down_file_conn:
            return False
        return True

    def run(self):
        pass

    def execute(self,shell):
        stdin, stdout, stderr = self.conn.exec_command(shell)
        print stdout
        print "-------------------------------------------"
        return stdout.readlines()

    def put_file(self,localfile,remotefile):
        print u"开始上传文件"
        self.up_down_file_conn.put(localfile,remotefile)

    def get_file(self,remotefile,localfile):
        print u"开始下载文件"
        self.up_down_file_conn.get(remotefile,localfile)

    def execute_close(self):
        try:
            self.conn.close()

            print u"%s对象结束，调用execute_close关闭方法" % self.ip
        except Exception,e:
            print u"%s已经conn关闭了" % self.ip
    def sftp_close(self):
        try:
            self.up_down_file_conn.close()

            print u"%s对象结束，调用sftp_close关闭方法" % self.ip
        except Exception,e:
            print u"%s已经conn关闭了" % self.ip
    def __del__(self):
        self.execute_close()
        self.sftp_close()

class Docker_fenpei_ip(F_bushu):
    def run(self,shell):
        rs = self.execute(shell=shell)
        return rs