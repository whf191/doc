#!/usr/bin/python2.7
#coding=utf-8
import  os,logging,urllib
import datetime,time
#进入到脚本本身目录..
os.chdir(os.path.split(os.path.realpath(__file__))[0])

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename=__file__+".log",
                filemode='a')

def send_wexin(msg):
    """
    curl -s  "192.168.0.77/send_weixin/?content=$host  restart 9001  port time:$shijian"

    :param msg:
    :return:
    """
    url = "http://192.168.0.77/send_weixin/?content='%s'&wxzh=wanwan"
    url_weixin = urllib.urlopen(url=url % msg)


def check_mysql():
    state = "running"
    mysql_exec = os.popen("/etc/init.d/mysqld status")
    mysql_result = mysql_exec.read()
    if state not in mysql_result:
        logging.error(u"mysql没有启动,启动mysql,time:%s" % datetime.datetime.today())
        os.system("/etc/init.d/mysqld start")
        logging.error(u"完成mysql启动,time:%s" % datetime.datetime.today())
        send_wexin("0.77 mysql restart")
    else:
        logging.info(u"mysql正常运行:%s" % datetime.datetime.today())

def check_uwsgi():
    check_cmd = "ps -ef | grep uwsgi8000 | grep -v grep |wc -l"
    uwsgi_exec = os.popen(check_cmd)
    uwsgi_result = int(uwsgi_exec.read().strip())
    if uwsgi_result  < 1:
        logging.error(u"uwsgis没有启动,进入/root/uwsgis ,time:%s" % datetime.datetime.today())
        os.chdir("/root/uwsgis")
        os.system("/bin/bash start.uwsgi")
        logging.error(u"完成uwsgis启动,time:%s" % datetime.datetime.today())
        send_wexin("0.77 uwsgi restart")
    else:
        logging.info(u"uwsgi正常运行:%s" % datetime.datetime.today())

def check_nginx():
    check_cmd = "ps -ef | grep nginx | grep -v grep |wc -l"
    cmd_exec = os.popen(check_cmd)
    cmd_result = int(cmd_exec.read().strip())
    if cmd_result <1:
        logging.error(u"nginx没有启动,启动nginx,time:%s" % datetime.datetime.today())
        os.system("/usr/local/nginx/sbin/nginx")
        logging.error(u"完成nginx启动,time:%s" % datetime.datetime.today())
        send_wexin("0.77 nginx restart")
    else:
        logging.info(u"nginx正常运行:%s" % datetime.datetime.today())


def run():
    while True:
        check_mysql()
        check_nginx()
        check_uwsgi()
        time.sleep(120)

if __name__ == '__main__':
    run()