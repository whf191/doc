#!/usr/bin/python
#coding=utf-8
import subprocess,os,time


def yibu_call(path,host,logging):
    logging.info("开始同步这个月:%s" % path)
    cmd = "rsync -aPR %s %s:/" % (path, host)
    subprocess.call(cmd,shell=True)
    logging.info("完成同步这个月:%s" % path)

def rsysnc_month(path,host,logging):
    """
    月份全部同步...

    :param path:
    :param host:
    :param logging:
    :return:
    """
    yibu_call(path=path,host=host,logging=logging)

def wait_tongbu(path,logging):
    """
    检查path路径是否存在，如果存在返回为真，假就wait吧...
    目的:
       避免pyinotify加载目录存才在,出现错误

    :param path:
    :return:
    """
    while True:
        state = os.path.isdir(path)
        if state:
            logging.info("路径:%s存在，程序继续执行..." % path)
            break
        else:
            logging.error("路径:%s不存在，延迟10分钟扫描" % path)
            time.sleep(600)




if __name__ == '__main__':
    pass
