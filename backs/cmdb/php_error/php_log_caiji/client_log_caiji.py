#!/usr/bin/python
#coding=utf-8
import json,datetime,time
import tail
import  os,sys
from tasks import log,man_log
from get_hostname import hostname

class client_log_caiji(object):
    """
       客户端启动方法:
      python logcaiji_client.py & 异步客户端...
      通过任务的tasks异步回调写入,rabbitmq队列
    """

    def __init__(self,tail,filename):
        self.tail = tail
        self.filename = filename
        self.hostname = hostname()
    def tailf(self):
        t = tail.Tail(self.filename)
        t.register_callback(self.man_log_exec)
        t.follow()

    def  log_exec(self,msg):
        try:
            msg= json.loads(msg)
            log.delay(msg)
        except Exception,e:
            with open("/var/log/tasks.log", "a") as f:
                f.write("""state:%s,content:%s \n""" % (str(e), msg))


    def man_log_exec(self,msg):
        """慢日志处理方法"""
        print msg
        if  len(msg.strip())  != 0:
            print 1111
            msg_json = {"hostname": self.hostname, "msg": msg}
            try:
                man_log.delay(msg_json)
            except Exception,e:
                with open("/var/log/tasks.log", "a") as f:
                    f.write("""man_log_state:%s,content:%s \n""" % (str(e), msg))


    def run(self):
        """
        主程序调用
        :return:
        """
        self.tailf()

def is_file(filename):
    while True:
        if os.path.isfile(filename):
            break
        else:
            time.sleep(10)

if __name__ == '__main__':
    filename_base = "/usr/local/nginx/logs/"
    today = str(datetime.date.today())
    name = "php-slow.log"
    #filename  = filename_base + today + "/" + name
    filename = filename_base + name
    is_file(filename)

    caiji = client_log_caiji(tail,filename=filename)
    caiji.run()
















