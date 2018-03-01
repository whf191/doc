#!/usr/bin/python
#coding=utf-8
import time
from celery import Celery
from  duilieguolvduan import postlog
import json

"""
工人启动方式..
celery -A tasks worker --loglevel=info


python2.6安装pip install celery==3.1.25
export C_FORCE_ROOT="true"

broker
amqp://guest@192.168.0.77//

redis://192.168.0.110:6379/0"

"""


app = Celery("tasks",broker="amqp://guest@192.168.0.77//")


@app.task
def log(msg):
    result = postlog(msg,url="http://192.168.0.77/postlog/")
    if result != "success":
        with open("/var/log/tasks.log", "a") as f:
            f.write("""state:%s,content:%s \n""" % (result, json.dumps(msg)))
        return result

    return result
