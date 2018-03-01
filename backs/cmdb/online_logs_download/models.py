#coding=utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class logsdownload(models.Model):
    name = models.CharField(max_length=255,verbose_name="项目")
    log_dir = models.CharField(max_length=255,verbose_name="日志存放路径")
    war_file = models.CharField(max_length=255,verbose_name="war包文件")
    user_id = models.ForeignKey(User)
    create_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = '日志下载'
        verbose_name_plural = '日志下载'




