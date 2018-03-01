#coding=utf-8
from __future__ import unicode_literals
from django.shortcuts import render,HttpResponse,HttpResponsePermanentRedirect,render_to_response
from .models import  *
from django.contrib.auth import authenticate
import json
# Create your views here.

def get_hosts(request):
    #print dir(request)
    if  request.method == "POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        user = authenticate(username=username,password=password)
        hosts_list = []
        if user  is  not None:
            if user.is_active:
                buhog = bind_users_hosts.objects.get(user_id=user)
                buhog_many_to_many =  buhog.hosts_id.all()
                for i in buhog_many_to_many:
                    hosts_list.append([i.hostname,i.hostip,i.hostport,i.hostuser,i.hostspassword])
                j = json.dumps(hosts_list)
                return HttpResponse(j)

    return HttpResponse(None)

def post_log(request):
    if request.method == "POST":
        username = request.POST.get("username",None)
        hostip  = request.POST.get("hostip",None)
        host_cmd = request.POST.get("host_cmd",None)
        print username,hostip,host_cmd
        # s = shenji(username=username,hostip=hostip,host_cmd=host_cmd)
        # s.save()
        return HttpResponse(1)
    return HttpResponse(0)

def get_gongong_shell(request):
    gg = gongong_shell.objects.all()
    gg = [ [i.mulu,i.sfile,i.dfile]  for i in gg]
    gg = json.dumps(gg)
    print json.loads(gg)
    return HttpResponse(gg)

def get_zhuji_mulu_wenjian(request):
    username = request.GET.get("username",None)
    hostip = request.GET.get("hostip",None)
    username="admin"
    hostip = "192.168.20.40"
    if username and hostip:
        try:
            s_hostip = hosts.objects.get(hostip=hostip)
            s_username = User.objects.get(username=username)
            rs = mulu_sfile_dfile.objects.filter(hosts_id=s_hostip,createuser=s_username)
        except Exception,e:
            return HttpResponse(json.dumps([]))
        gzmw = [[i.mulu,i.sfile,i.dfile,i.createuser.username] for i in rs]
        gzmw = json.dumps(gzmw)
        return HttpResponse(gzmw)

