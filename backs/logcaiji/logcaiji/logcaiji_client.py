#!/usr/bin/python
# coding=utf-8
import tail
import json, sys, multiprocessing
from tasks import log


s = {"host": "", "url": "","state":"","ip":"","cookie":""}

def log_exec(msg):
    """回调函数，执行task模块的log任务"""
    try:
        s["content"] = msg
        log.delay(s)
        return True
    except Exception, e:
        print e
        return False

def tailf(filename, s=1):
    t = tail.Tail(filename)
    t.register_callback(log_exec)
    t.follow(s=s)

def main(l1):
    """  多进程抽取文件 """
    for i in l1:
        s['tag'] = i[0]
        filename = i[1]
        p = multiprocessing.Process(target=tailf, args=(filename,))
        p.start()


def main2(filename):
    """  单进程抽取文件 """
    tailf(filename)

if __name__ == '__main__':
    # main([["iptables", "/var/log/iptables.log"]])
    #python logcaiji_client.py & 异步客户端...
    #通过任务的tasks异步回调写入,rabbitmq队列
    """
    芹菜的工作流程是先执行数据采集，后工作人员执行
    
    """
    s['tag']="iptab"
    main2("/var/log/iptables.log")


