#coding=utf-8
from __future__ import unicode_literals
from django.contrib import admin
from .models import  *
from  .htmls.project_models import logs_download
# Register your models here.


class logsdownload_zdy(admin.ModelAdmin):
    list_display = ('name','logs')

    #用户能看到自己的东西
    def get_queryset(self, request):
        qs = super(logsdownload_zdy, self).get_queryset(request)

        if  request.user.is_superuser:
            return qs

        get_userid = logsdownload.objects.filter(user_id=request.user.id)

        return get_userid

    #封锁普通用户为只读
    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser :
            readonly_fields = ['name','log_dir','war_file','user_id']
            return readonly_fields

        return super(logsdownload_zdy,self).get_readonly_fields(request,obj=None)


    def logs(self,obj):
        pk = obj.pk
        return logs_download(pk=pk)

    logs.short_description = "log下载"
    logs.allow_tags = True


    def war(self,obj):
        return "obj"

    war.short_description = "war下载"
    war.allow_tags = True



admin.site.register(logsdownload,logsdownload_zdy)


