#!/usr/bin/python
#coding=utf-8
__author__ = "wanwan"
from django.shortcuts import render_to_response,HttpResponse
from .xuliehua import My_db_diy
import random

my = My_db_diy()


def hello(req):

    return HttpResponse(my.all("users"))


def add(req):

    ad = my.add("users",{"name":"w%s" % random.randint(1,100),"age":random.randint(1,100)})
    my.commit()
    if add:
        return HttpResponse("添加成功")
    else:
        return HttpResponse("添加失败")

def delete(req):
    pk = req.GET.get("pk",None)
    table = req.GET.get("table",None)
    if pk and table:
        try:
            my.remove_index(table,int(pk))
            my.commit()
            return HttpResponse(True)
        except Exception,e:
            return HttpResponse(Exception)

    else:
        return HttpResponse(False)