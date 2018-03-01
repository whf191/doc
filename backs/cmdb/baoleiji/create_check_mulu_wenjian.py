#!/usr/bin/python
#coding=utf-8
import shutil
import os
import  sys,json,urllib

class create_check_mulu_wejian(object):
    """  mulu ,,wenjian 必须是个二元列表,像这样[['目录','源文件','目标文件']]
    此对对象做两部分操作，第一部分是创建公共shell目录，第二部分，创建日志目录和删除日志文件

    """

    def __init__(self,mulu):
        self.mulu = mulu

    def check_mulu(self):
        if len(self.mulu) == 0:
            #传过来的目录是个空的，退出当前python
            print "kong..."
            return sys.exit(1)
        dirlist=[]
        print self.mulu
        for i in self.mulu:
            if not os.path.isdir(i[0]):
                dirlist.append(i)
        #检测的文件如果都存在，返回一个真
        if len(dirlist) == 0:
            return True
        else:
            #否则返回需要创建的目录
            return dirlist

    def create_mulu(self):
        get_mu = self.check_mulu()
        print get_mu
        if isinstance(get_mu,list):
            for i in get_mu:
                print i
                os.system("mkdir -p  %s" % i[0])
            return u"目录创建完毕%s" % get_mu
        else:
            return u"目录存在，不用创建"

    def check_file(self):
        if len(self.mulu) == 0:
            print u"传过来的文件是空...,退出程序"
            return sys.exit(1)
        wenjianlist= []
        for i in self.mulu:
            if not os.path.isfile(i[2]):
                wenjianlist.append(i)
        if len(wenjianlist) == 0:
            return  True
        else:
            return wenjianlist

    def copy_file(self):
        get_wj = self.check_file()
        if isinstance(get_wj,list):
            #拷贝源文件到目标文件
            for i in get_wj:
                shutil.copy(i[1],i[2])
            return u"拷贝文件完毕"
        return u"文件都存在，不需要拷贝"

    def check_logfile(self,logfile):
        if len(logfile) == 0:
            print u"传过来的日志文件为空，退出"
            return sys.exit(1)
        logfilelist = []
        for i in logfile:
            if not os.path.isfile(i[2]):
                logfilelist.append(i)
        if len(logfilelist) == 0:
            return True
        else:
            return logfilelist

    def create_file(self,logfile):
        #"判断logfile文件是否存在.."
        logfile = logfile
        get_lf = self.check_logfile(logfile=logfile)
        if isinstance(get_lf,list):
            if len(logfile) == 0:
                print "list对象为空..退出"
                return sys.exit(1)
            for i in get_lf:
                os.system("ln %s %s" % (i[1],i[2]))
            return u"硬连接日志文件完成..."
        if not get_lf:
            print  u"不是一个list对象"
            return sys.exit(1)

    def del_file(self,username,logfile):
        w_user = os.popen("w|grep -c '%s' " % username)
        w_user = w_user.read().strip()
        if int(w_user) > 1 :
            print w_user
            print u"用户未退出登录，不删除文件"
            return True
        elif int(w_user) == 1 :
            if not isinstance(logfile,list):
                print u"不是一个list对象，退出"
                return sys.exit(1)
            for i in logfile:
                try:
                    print u"开始删除文件%s" % i[2]
                    os.remove(i[2])
                except Exception,e:
                    print e
            return u"删除目标文件完成"

    def chroot(self,username):
        os.system("chroot /%s/test" % username)
        print "hello, end...."
    # def __del__(self):
    #     os.system("rm -rf /root/test")


def get_urlopen(url):
    """ 返回json对象"""
    rs_u = urllib.urlopen(url)
    rs = rs_u.read()
    rs = json.loads(rs)
    return rs

def get_user():
    gu = os.popen("pwd")
    rs_gu = gu.read()
    rs_gu_list = rs_gu.split("/")
    rs_gu_list = rs_gu_list[-1]
    rs_gu_list = rs_gu_list.split("\n")
    return rs_gu_list[0]

if __name__ == '__main__':

    rs_shell = get_urlopen("http://192.168.1.31:8000/get_gongong_shell/")
    rs_logfile = get_urlopen("""http://192.168.1.31:8000/get_zhuji_mulu_wenjian/?username="admin"&hostip="192.168.20.40" """)
    ccmw = create_check_mulu_wejian(rs_shell)
    ccmw.del_file(get_user(), rs_logfile)
    ccmw.create_mulu()
    ccmw.copy_file()
    ccmw.create_file(logfile=rs_logfile)
    ccmw.chroot(get_user())


