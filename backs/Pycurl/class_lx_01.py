#coding=utf-8
from __future__ import unicode_literals



class My(object):
    gg = 20
    def __init__(self):
        self.chushihua="My..."

    def bat(self):
        self.bat2="百度 阿里 腾讯"

    def fangfa(self):
        print "fangfa"


# my1 = My()
# print my1.chushihua
# my1.bat()
# print my1.bat2
# print my1.fangfa(),my1.gg
#
import requests
import sys
url_list=["http://www.meilele.com","http://www.kkkbaidu222.com","http://www.kkbaidu222.com","http://www.kkkbaidu222.com"]
num=0
str_url_list = " "
for i in url_list:
    try:
        r = requests.get(i)
        rs_seconds =  r.elapsed.seconds
        if  rs_seconds != 0:
            str_url_list += i
            num+=1
    except Exception,e:
        str_url_list +=i
        num+=1
if num !=0:
    print "%s no open!!!!!!! .." % str_url_list
    sys.exit(2)
else:
    print "%s is ok..." % " ".join(url_list)
    sys.exit(0)

