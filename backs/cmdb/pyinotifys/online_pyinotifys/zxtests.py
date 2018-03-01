#/usr/bin/python
#coding=utf-8
import logging
import pyinotify
import commands
import os
from date_format import get_ymd,last_month
from tongbu_month import rsysnc_month,wait_tongbu

#进入到脚本本身目录..
os.chdir(os.path.split(os.path.realpath(__file__))[0])

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='zx_pyinotify.log',
                filemode='a')


class EventHandler(pyinotify.ProcessEvent):

    def process_IN_CREATE(self,raw_event):
        sfile =  raw_event.pathname
        dfile = sfile

        print sfile
        if self._rsync(sfile=sfile,dfile=dfile):
            return True
        return False

    def _rsync(self,sfile,dfile,host="192.168.0.16"):
        cmd = "rsync -avP %s %s:/" % (sfile,host)
        state, neirong = commands.getstatusoutput(cmd=cmd)

        if state != 0:
            logging.error("state:%s sfile:%s dfile:%s neirong:%s" % (state,sfile,dfile,neirong))
            return False
        logging.info("state:%s sfile:%s dfile:%s neirong:%s" % (state,sfile,dfile,neirong))
        return True


if __name__ == '__main__':

    path = '/web/meilele_100514/zximages/images/%s'
    path_last_mouth = path % last_month()
    path_loacl_mouth = path % get_ymd()
    host = '192.168.0.16'

    wait_tongbu(path=path_loacl_mouth, logging=logging)

    rsysnc_month(path=path_last_mouth,host=host,logging=logging)
    rsysnc_month(path=path_loacl_mouth, host=host, logging=logging)
    logging.info("执行主程序pyinotify")
    wm = pyinotify.WatchManager()

    mask = pyinotify.IN_CREATE
    handler = EventHandler()
    notifier = pyinotify.Notifier(wm,handler)
    wdd = wm.add_watch(path=[path_loacl_mouth],mask=mask,rec=True,auto_add=True)
    notifier.loop()
