#!/usr/bin/python
#coding=utf-8
import time
from celery import Celery
from  postlog import postlog,post_man_log
import json

"""
pip install supervisor
supervisord -c /etc/supervisord.conf

vi /usr/lib/python2.6/site-packages/supervisor-3.3.3-py2.6.egg-info/requires.txt
工人启动方式..
celery -A tasks worker --loglevel=info


python2.6安装pip install celery==3.1.25
export C_FORCE_ROOT="true"

broker
amqp://guest@192.168.0.77//

redis://192.168.0.110:6379/0"

"""




app = Celery("tasks",broker="amqp://admin:admin@192.168.0.77//")


@app.task
def log(msg):
    try:
        result = postlog(msg, url="http://ywweixin.meilele.com/phperror/")
        if result != "ok":
            with open("/var/log/tasks.log", "a") as f:
                f.write("""state:%s,content:%s \n""" % (result, msg))
    except Exception,e:
        with open("/var/log/tasks.log", "a") as f:
            f.write("""state:%s,content:%s \n""" % (str(e),msg))

@app.task
def man_log(msg):
    try:
        result = post_man_log(msg,url="http://ywweixin.meilele.com/postmanlog/")
        if result != "ok":
            with open("/var/log/tasks.log", "a") as f:
                f.write("""man_log_state:%s,content:%s \n""" % (result, msg))
    except Exception,e:
        with open("/var/log/tasks.log", "a") as f:
            f.write("""man_log_state:%s,content:%s \n""" % (str(e),msg))
