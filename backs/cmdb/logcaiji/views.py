#coding=utf-8
from  __future__  import  unicode_literals
from django.shortcuts import render_to_response,HttpResponse,HttpResponseRedirect
from .models import logs,cpuload
import json


def postlog(request):
    tag =  request.POST.get("tag",None)
    content = request.POST.get("content",None)
    if tag and content:
        lg = logs(leixing=tag,neirong=content)
        lg.save()
        return HttpResponse("success")
    return HttpResponse("faile")

def postload(request):
    if request.method == "POST":
        load = request.POST.get("load","000")
        hostname = request.POST.get("hostname","000")
        if load != "000":
            one,five,fifteen = load.split(",")
            try:
                cpuload_write = cpuload(hostname=hostname,one=one,five=five,fifteen=fifteen)
                cpuload_write.save()
                return HttpResponse("success")
            except Exception,e:
                return HttpResponse("fail")
        return HttpResponse("load fail")
    return HttpResponse("not post")