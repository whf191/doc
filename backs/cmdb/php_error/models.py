#coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class phperror(models.Model):
    host = models.CharField(max_length=255,blank=True,verbose_name="主机")
    ip = models.CharField(max_length=255, blank=True, verbose_name="ip")
    log = models.TextField(blank=True, verbose_name="log")
    url = models.CharField(blank=True, max_length=255, verbose_name="log_type")
    log_type = models.CharField(blank=True,max_length=255,verbose_name="log_type")
    project = models.TextField(blank=True,max_length=255,verbose_name="project")
    cookie =  models.TextField(blank=True,verbose_name="cookie")
    other = models.TextField(blank=True, verbose_name="other")
    time  = models.CharField(max_length=60,blank=True)

    class Meta:
        verbose_name = u'php错误记录'
        verbose_name_plural = u'php错误记录'

class phperror404(models.Model):
    host = models.CharField(max_length=255,blank=True,verbose_name="主机")
    ip = models.CharField(max_length=255, blank=True, verbose_name="ip")
    log = models.TextField(blank=True, verbose_name="log")
    url = models.CharField(blank=True, max_length=255, verbose_name="log_type")
    log_type = models.CharField(blank=True,max_length=255,verbose_name="log_type")
    project = models.TextField(blank=True,max_length=255,verbose_name="project")
    cookie =  models.TextField(blank=True,verbose_name="cookie")
    other = models.TextField(blank=True, verbose_name="other")
    time = models.CharField(max_length=60,blank=True)

    class Meta:
        verbose_name = u'php错误记录404'
        verbose_name_plural = u'php错误记录404'

class manlog(models.Model):
    host = models.CharField(max_length=255,blank=True,verbose_name="主机名")
    msg = models.TextField(blank=True,verbose_name="log")
    create_date = models.DateTimeField(auto_now=True)
    date = models.DateField(auto_now=True)

    class Meta:
        verbose_name = u'php慢日志'
        verbose_name_plural = u'php慢日志'