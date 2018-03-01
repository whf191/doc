#coding=utf-8
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib import messages
from .models import *
from .htmls.queding_peizhi_moban import qpm,qcc,ccs,remote_exec_script
import time,uuid,ping,json
from .remote_paramiko.remote_paramiko import remote_paramiko
# Register your models here.

class managecontainer_zdy(admin.ModelAdmin):
    list_display = ('id','alias','runing','openport','dockerimages_id','containerip_id','registerscript_id11','state11')
    fields = ('openport','dockerhost_id','dockerimages_id','containerip_id','container_username','container_password','apptype_id','registerscript_id','extensions_directory','container_id')
    search_fields = ('openport','alias')
    list_filter =  ('openport','dockerhost_id','dockerimages_id','containerip_id','apptype_id','registerscript_id')

    def state11(self,obj):
        pk = obj.pk

        if obj.state1 == "1":
            return qpm(pk=pk)

        elif obj.state1 == "2":
            return qcc(pk=pk,pk_time= pk,container_name=obj.alias,container_host="%s/%s" % (obj.dockerhost_id.name,obj.dockerhost_id.ip),container_port=obj.openport,container_script=obj.registerscript_id.name)

        elif obj.state1 == "3":
            return remote_exec_script(pk=pk)
        else:
            return obj.state1

    state11.short_description = "容器状态"
    state11.allow_tags = True

    def registerscript_id11(self,obj):
        return ccs(pk=obj.pk)
    registerscript_id11.short_description = "修改脚本"
    registerscript_id11.allow_tags = True

    def runing(self,obj):
        pk = obj.pk
        ip = obj.containerip_id.ip
        state1 = obj.state1
        if state1 == "3":
            rs = ping.quiet_ping(ip,timeout=0.6)
            if rs[0] != 0:
                return """<img  src="/static/guanbi.png" ><b>off</b>"""
            else:
                return  """<img  src="/static/open.png" ><b>open</b>"""
        return "unknown"

    actions = ['run_container','stop_container']

    def run_container(self,request,queryset):
        for  i in queryset:
            state1 = i.state1
            if state1 == "3":
                docker_username = i.dockerhost_id.docker_username
                docker_password = i.dockerhost_id.docker_password
                container_id = i.container_id[:11]
                containerip_id = i.containerip_id.ip
                dockerhost = i.dockerhost_id.ip
                mask = i.dockerhost_id.mask
                gateway = i.dockerhost_id.gateway
                messages.info(request,"%s%s%s%s" % (containerip_id,mask,gateway,container_id))
                t = remote_paramiko(dockerhost,docker_username,docker_password)
                rs = t.run("docker restart %s" % container_id)
                rs = t.run("pipework  br0 %s  %s/%s@%s " % (container_id, containerip_id,mask,gateway) )

                messages.info(request,json.dumps(rs))

            else:
                messages.error(request,"ID:%s,容器还未创建" % i.pk)

    runing.allow_tags = True


    def stop_container(self,request,queryset):
        for i in queryset:
            state1 = i.state1
            if state1 == "3":
                docker_username = i.dockerhost_id.docker_username
                docker_password = i.dockerhost_id.docker_password
                container_id = i.container_id[:11]
                containerip_id = i.containerip_id.ip
                dockerhost = i.dockerhost_id.ip
                mask = i.dockerhost_id.mask
                gateway = i.dockerhost_id.gateway
                messages.info(request, "%s%s%s%s" % (containerip_id, mask, gateway, container_id))
                t = remote_paramiko(dockerhost, docker_username, docker_password)
                rs = t.run("docker stop %s" % container_id)
                messages.info(request, json.dumps(rs))

            else:
                messages.error(request, "ID:%s,容器还未创建" % i.pk)

    run_container.short_description  = "启动容器"

    stop_container.short_description = "关闭容器"

    # 重写外键方法
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):

        if db_field.name == "containerip_id":
            kwargs['queryset'] = containerip.objects.exclude(active=True)
        return super(managecontainer_zdy, self).formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(idc)
admin.site.register(dockerimages)
admin.site.register(dockerhost)
admin.site.register(containerip)
admin.site.register(apptype)
admin.site.register(registerscript)
admin.site.register(managecontainer,managecontainer_zdy)

