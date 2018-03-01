#coding=utf-8
from __future__ import unicode_literals
from django.shortcuts import HttpResponse,HttpResponseRedirect
from .models import managecontainer,containerip,registerscript
from docker_api.docker_api import  docker_api
from docker import errors
import json
import os
from .remote_paramiko.remote_paramiko import remote_paramiko
# Create your views here.

def is_container_config(request):
    if request.method == "POST":
        pk = request.POST.get("pk",None)
        if pk:
            try:
                mc = managecontainer.objects.get(id=pk)
                apptype_name = mc.apptype_id.name
                ip_name = mc.containerip_id.ip
                port_name = mc.openport
                if mc.state1 == "1":
                    mc.state1 = "2"
                    mc.alias = "%s_%s_%s" % (apptype_name,ip_name,port_name)
                    mc.save()
                    return HttpResponse("配置保存,可以生成容器了")
                else:
                    return HttpResponse("当前状态为:%s" % mc.state1)

            except Exception,e:
                return HttpResponse("参数错误，没有找到这条数据")

    return HttpResponse("not post")

def get_contalner_script(request):
    if request.method == "POST":
        pk = request.POST.get("pk",None)
        sc_val = request.POST.get("sc_val",None)
        if pk and not sc_val:
            try:
                mc = managecontainer.objects.get(id=pk)
                result = mc.registerscript_id.shell
                print result
                return HttpResponse(result)
            except Exception,e:
                return HttpResponse("参数错误，没有找到这条数据")

        if pk and sc_val:
            print "__________________"
            print pk,sc_val
            try:
                mc = managecontainer.objects.get(id=pk)
                script_id = mc.registerscript_id.id
                rs = registerscript.objects.get(pk=script_id)
                rs.shell = sc_val
                rs.save()
                return HttpResponse("脚本保存成功")
            except Exception,e:
                print e
                return HttpResponse("参数错误，脚本保存失败")

    return HttpResponse("not post")


def is_container_create(request):

    if request.method == "POST":
        pk = request.POST.get("pk", None)
        if pk:
            try:
                mc = managecontainer.objects.get(pk=pk)
                ip_id = mc.containerip_id.pk
                print ip_id
                hostname = mc.alias
                name = hostname
                hostname = hostname.split('_')
                hostname = hostname[0] +'-' + hostname[1].split(".")[-1]
                base_url = "tcp://%s:2375" % mc.dockerhost_id.ip
                image = mc.dockerimages_id.name
                external_directory = mc.extensions_directory
                d_api = docker_api(base_url=base_url)
                create_container = d_api.create_container(image=image, external_directory=external_directory,
                                                          hostname=hostname, name=name)
                # 保存创建容器后的ID
                mc.container_id = create_container
                mc.state1 = 3
                mc.save()
                # 更改IP标记为使用
                c_ip = containerip.objects.get(pk=ip_id)
                c_ip.active = True
                c_ip.save()

            except errors.APIError,e:

                return HttpResponse(error_json(1,e.__str__()))

            except Exception,e:

                return HttpResponse(error_json(1,e.__str__()))

            return HttpResponse(error_json(0,create_container))

    return HttpResponse("not post")

def error_json(state,msg):
    result = {'state': state, 'msg': msg}
    result1 = json.dumps(result)
    return result1

def remote_call_script(request):
    if request.method == "POST":
        pk = request.POST.get("pk",None)
        state = request.POST.get("state",None)
        if pk and state:
            if state == "start":
                mc = managecontainer.objects.get(pk=pk)
                container_ip = mc.containerip_id.ip
                script_name = mc.registerscript_id.name
                container_username = mc.container_username
                container_password = mc.container_password
                script = mc.registerscript_id.shell
                with open(script_name,'w') as f:
                    f.write(script)
                #得到脚本完整路径
                script_file = os.getcwd() + os.sep + script_name
                remote_script_file = "/tmp/" + script_name
                t = remote_paramiko(container_ip,container_username,container_password)
                t.put_file(localfile=script_file,remotefile=remote_script_file)
                rs = t.run("/bin/bash   %s" % remote_script_file)

                return HttpResponse("%s" % "   <br>".join(rs))
            else:
                return HttpResponse("暂时不支持")


        else:
            return  HttpResponse("参数不符号")



    return HttpResponse("not post")
