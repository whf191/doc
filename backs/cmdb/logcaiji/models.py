#coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class  logs(models.Model):
    leixing = models.CharField(max_length=30)
    neirong = models.TextField()

    def __unicode__(self):
        return "%s" % self.leixing

    class Meta:
        verbose_name = u'日志采集'
        verbose_name_plural = u'日志采集'

class cpuload(models.Model):
    hostname = models.CharField(max_length=255, verbose_name="主机名字")
    one = models.CharField(max_length=50,verbose_name="1分钟")
    five = models.CharField(max_length=50,verbose_name="5分钟")
    fifteen = models.CharField(max_length=50,verbose_name="15分钟")
    datetime = models.DateTimeField(auto_now=True)
    date = models.DateField(auto_now=True)
    def __unicode__(self):
        return "%s" % self.hostname

    class Meta:
        verbose_name = u'cpuload'
        verbose_name_plural = u'cpuload'
