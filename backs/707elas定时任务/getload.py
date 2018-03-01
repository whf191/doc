#!/usr/bin/python
#coding=utf-8
import re,os,json,urllib,sys
"""
采集cpuload值...

nrpe:
  echo 'command[getload]=/usr/local/nagios/libexec/getload.py' >>/usr/local/nagios/etc/nrpe.cfg


"""



def cpuload():
    cpu = os.popen("w")
    cpu = cpu.readline()
    cpu =  cpu.split()
    cpu = cpu[-3:]
    return cpu

def putcpuload(url,data):
    data = urllib.urlencode(data)
    post_url = urllib.urlopen(url=url,data=data)
    return post_url.read()


if __name__ == '__main__':
    url = "http://ywweixin.meilele.com/postload/"
    data = {'load':"".join(cpuload()),"hostname":os.popen("hostname").read().strip()}
    result = putcpuload(url=url,data=data)
    if result != "success":
        print "load save fail"
        sys.exit(2)
    else:
        print "load save success"
        sys.exit(0)

