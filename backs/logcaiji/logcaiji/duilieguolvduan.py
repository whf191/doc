#!/usr/bin/python
#coding=utf-8
import  urllib
from logging_01 import log_jilu

def postlog(data,url="http://192.168.1.31:8000/postlog/"):
    try:
        parmas = urllib.urlencode(data)
        f = urllib.urlopen(url,parmas)
        return f.read()
    except Exception,e:
        with open("/var/log/postlog.log",'a') as f2:
            f2.write(str(e)+ url +"\n"  )
        return "faile"

if __name__ == '__main__':
        pass










