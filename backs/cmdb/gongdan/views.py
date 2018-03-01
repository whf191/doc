#coding=utf-8
from __future__ import unicode_literals
from django.shortcuts import render,HttpResponse,HttpResponseRedirect,HttpResponsePermanentRedirect,render_to_response
from .models import *

def gongdan_shenqing(request,obj_id,times):
    pk = shijian.objects.get(pk=int(obj_id))
    print pk,"++++++++++++++++++++++++++++"
    if  pk.is_shenqing == '0':
        pk.is_shenqing='1'
        pk.save()
    return HttpResponse("ok..")


def gongdan_chuli(request,obj_id,times):
    pk = shijian.objects.get(pk=int(obj_id))
    if pk.is_shenqing == "1":
        pk.is_shenqing = "2"
        pk.save()
    return  HttpResponse("ok...")