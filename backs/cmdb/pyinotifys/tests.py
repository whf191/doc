#/usr/bin/python
#coding=utf-8
import logging
import pyinotify
import commands
import os

#进入到脚本本身目录..
os.chdir(os.path.split(os.path.realpath(__file__))[0])

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='pyinotify.log',
                filemode='a')


class EventHandler(pyinotify.ProcessEvent):

    def process_IN_CREATE(self,raw_event):
        sfile =  raw_event.pathname
        dfile = sfile

        print sfile
        #if self._rsync(sfile=sfile,dfile=dfile):
        #    return True
        #return False


    def _rsync(self,sfile,dfile,host="192.168.20.67"):
        cmd = "rsync -avzP %s %s:%s" % (sfile,host,dfile)
        state, neirong = commands.getstatusoutput(cmd=cmd)

        if state != 0:
            logging.error("state:%s sfile:%s dfile:%s neirong:%s" % (state,sfile,dfile,neirong))
            return False
        logging.info("state:%s sfile:%s dfile:%s neirong:%s" % (state,sfile,dfile,neirong))
        return True


if __name__ == '__main__':
    wm = pyinotify.WatchManager()

    mask = pyinotify.IN_CREATE
    handler = EventHandler()
    notifier = pyinotify.Notifier(wm,handler)
    wdd = wm.add_watch(path="/root/11",mask=mask,rec=True,auto_add=True)
    notifier.loop()