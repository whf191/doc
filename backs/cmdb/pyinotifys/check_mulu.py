#!/usr/bin/python
#coding=utf-8
import commands

def check_mulu(remotehost,dfile):
    """
    检查远程目录
    
    :param remotehost: 
    :param dfile: 
    :return: 
    """
    dfile_offset = dfile.rindex("/")
    difle_mulu = dfile[:dfile_offset]
    cmd = "ssh %s ls %s" % (remotehost,difle_mulu)
    result  = commands.getstatusoutput(cmd)
    return result





