#coding=utf-8
from __future__ import unicode_literals
from django.shortcuts import HttpResponse,render_to_response,HttpResponseRedirect
from .models import hosts


def gengxin_mima(request):
    if request.method =="POST":
        get_ip = request.POST.get("ip",None)
        get_pass = request.POST.get("pass",None)
        if get_ip is None:
            return  HttpResponse("get ip is none")
        try:
            ip = hosts.objects.get(hostip=get_ip)
            ip.hostspassword=get_pass
            ip.save()
            return HttpResponse("更新OK,IP:%s,pass:%s" % (get_ip,get_pass))
        except Exception,e:
            return HttpResponse("异常:%s" % e)