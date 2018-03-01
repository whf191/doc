#!/usr/bin/python
#coding=utf-8

import datetime,time,os,logging
#进入到脚本本身目录..
os.chdir(os.path.split(os.path.realpath(__file__))[0])

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='dingshi_task.log',
                filemode='a')


def dingshi_task(beigin_time,alter_seconds,dingshi,call_func_list=None):
    while True:
        beigin_time = beigin_time + alter_seconds
        print beigin_time
        time.sleep(1)

        str_now_datetime = beigin_time.strftime("%H%M%S")
        #logging.info(str_now_datetime)
        if str_now_datetime == dingshi:
            if call_func_list is None:
                logging.error(u"没有配置回调函数,dingshi:%s" % dingshi)
            else:
                logging.info(u"开始调用回调函数,dingshi:%s" %  dingshi)
                for i in call_func_list:
                    i()
                    logging.info(u"%s 完成回调函数调用,dingshi:%s" %  (i,dingshi))

def restat_els():
    logging.info(u"关闭elas")
    os.system(""" ansible elas -m shell -a "supervisorctl stop elas"   """)
    time.sleep(2)
    logging.info(u"启动elas")
    os.system(""" ansible elas -m shell -a  "supervisorctl start elas"  """)

def restart_rsyslog():
    logging.info(u"重启rsyslog...")
    os.system(""" ansible php_rsyslog -m shell -a " /usr/local/rsyslog_8.16.0/rsyslog-start.sh restart  m www event "
  """)
    logging.info(u"完成重启rsyslog...")

if __name__ == '__main__':
    """
    python2.6不支持shell管道符号操作
    
    elasticsearch = "su es -c '/usr/local/elasticsearch-2.2.0/bin/elasticsearch' "
    
    supervisord -c /etc/supervisord.conf  //启动supervisor
    supervisorctl [start,startus,stop] app
    
    """


    # 获取开始时间
    beigin_time = datetime.datetime.today()
    alter_seconds = datetime.timedelta(seconds=1)
    #配置每天定时任务执行时间
    dingshi = "011111"
    logging.info(u"定时任务开始执行...定时时间为:%s" % dingshi)
    dingshi_task(beigin_time, alter_seconds, dingshi, call_func_list=[restart_rsyslog,restat_els])
    logging.info(u"定时任务关闭...")

