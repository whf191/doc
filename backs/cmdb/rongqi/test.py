#coding=utf-8
from yuanchenglianjie import Docker_fenpei_ip
import time
external_directory = "%s_%s" % (22,int(time.time()))
yc = Docker_fenpei_ip('192.168.0.17', 'root', 'zb63DZE#Sp$Dk]q,&PbS')
yc.run("mkdir -p /var/opt/%s" % external_directory)