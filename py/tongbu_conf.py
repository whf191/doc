#!/usr/bin/python
#coding=utf-8
import threading,os,time

TEMPFILE="/tmp/rsysnc_nginx_2018123.conf"
LS_CONF = " ls /usr/local/nginx/conf/*.conf | grep -Ev 'nginx\.conf|fastcgi\.conf' >>%s    2>&1" % TEMPFILE
LS_JSON = "ls /usr/local/nginx/conf/*json >>%s   2>&1" % TEMPFILE
LS_LUA = "ls /usr/local/nginx/conf/*lua >>%s   2>&1" % TEMPFILE
ls = [LS_CONF,LS_JSON,LS_LUA]
iplist=[5,7,8,13,16,17,76]

lock = threading.Lock()
global_threads = 10
threads_count = 0

def add_thread_count():
    lock.acquire()
    global  threads_count
    threads_count +=1
    lock.release()

def del_thread_count():
    lock.acquire()
    global  threads_count
    if threads_count == 0:
        pass
    else:
        threads_count -= 1
    lock.release()


def startcmd(cmd):
    pipe = os.popen(cmd)
    sts = pipe.close()
    if sts is None:
        sts = 0
    else:
        sts = 404
    return sts

def new_iplist(iplist):
    ipnewlist = []
    for i in iplist:
        r = startcmd("ssh root@192.168.0.%s ls 2>&1" % i)
        if r == 0:
            ipnewlist.append(i)
        else:
            print  u"192.168.20.%s  is failed" % i

    return ipnewlist


def ls_file(ls):
    startcmd(">%s" % TEMPFILE)
    for i in ls:
        startus = startcmd(i)
        if startus !=0:
            print "%s is failed" % i

def  check_file(filename,ip):
    file_list = []

    for i in open(filename):
        i = i.strip()
        lmd5 = os.popen("md5sum %s 2>&1" % i).read().strip().strip().split()
        rmd5 = os.popen("ssh root@192.168.0.%s  md5sum  %s  2>&1" % (ip,i)).read().strip().split()
        if lmd5[0] not in rmd5:
            file_list.append(i)

    print "need is file",file_list
    return file_list


def rsysnc_file(TEMPFILE,ip):
    file_list = check_file(TEMPFILE,ip)
    for i in file_list:
        r = startcmd("""  /usr/bin/rsync -vzrtopgcI --progress -e ssh %s  root@192.168.0.%s:/usr/local/nginx/conf/ >/dev/nul 2>&1  """ % (i,ip))
        if r == 0:
            print "%s  %s is ok" % (i,ip)
        else:
            print "%s  %s is fail" % (i,ip)

    del_thread_count()

def nginx_reload(ip):
    r = startcmd(""" ssh root@192.168.0.%s "/usr/local/nginx/sbin/nginx -s reload"   """ % ip)
    if r == 0:
        print "host:192.168.0.%s nginx is reload  is ok " % ip
    else:
        print "host:192.168.0.%s nginx is reload  is fail " % ip
    if ip != "4":
        del_thread_count()

def rsync_thread(newiplist):

    t_take = []
    for i in newiplist:
        t1 = threading.Thread(target=rsysnc_file, args=(TEMPFILE, i))
        t_take.append(t1)

    for i in t_take:
        i.start()
        add_thread_count()
        while True:
            if threads_count < global_threads:
                break
            else:
                time.sleep(1)

    for i2 in t_take:
        i2.join()

def nginx_reload_thread(newiplist):
    t_take = []
    for i in newiplist:
        t1 = threading.Thread(target=nginx_reload,args=(i,))
        t_take.append(t1)

    for i in t_take:
        i.start()
        add_thread_count()
        while True:
            if threads_count < global_threads:
                break
            else:
                time.sleep(1)

    for i2 in t_take:
        i2.join()


def run():
    ls_file(ls)
    newiplist = new_iplist(iplist)

    rsync_thread(newiplist)

    nginx_reload_thread(newiplist)

    nginx_reload("4")

    print "rsysnc is end"

if __name__ == '__main__':
    """
    多线程同步，默认开启10个线程
    """
    run()



