#coding=utf-8
from __future__ import unicode_literals

from django.db import models
"""
表关系:
    1.机房 --> 2.主机类型 --> 3.主机 --> 4 事件 --> 5 主机事件日志

"""







class jifang(models.Model):
    name = models.CharField(max_length=255,verbose_name="机房")
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = '机房'
        verbose_name_plural = '机房'

class host_type(models.Model):
    jifang_id = models.ForeignKey(jifang,verbose_name="关联机房")
    name = models.CharField(max_length=255,verbose_name="主机类型")
    url = models.CharField(max_length=255,verbose_name="导航url")
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = '主机类型'
        verbose_name_plural = '主机类型'


class host(models.Model):
    host_type_id = models.ForeignKey(host_type,verbose_name="关联主机类型")
    ip = models.GenericIPAddressField(verbose_name="ip")
    name = models.CharField(max_length=255,verbose_name="主机名称")
    bind_shijian = models.ManyToManyField('shijian',verbose_name="主机事件绑定")
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = '主机'
        verbose_name_plural = '主机'


class shijian(models.Model):
    name = models.CharField(max_length=255,verbose_name="事件名称")
    value = models.CharField(max_length=255,verbose_name="事件值")

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = '事件'
        verbose_name_plural = '事件'

class shijian_log(models.Model):
    host_id = models.ForeignKey(host,verbose_name="关联主机")
    shijian_id = models.ForeignKey(shijian,verbose_name="关联事件")
    name = models.CharField(max_length=255,verbose_name="事件日志对应的UUID")
    create_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s(%s)" % (self.host_id,self.shijian_id)
    class Meta:
        verbose_name = '主机事件日志'
        verbose_name_plural = '主机事件日志'





