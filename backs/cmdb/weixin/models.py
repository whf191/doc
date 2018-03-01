#coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class leixing(models.Model):
    name = models.CharField(max_length=50,verbose_name="主机端口类型")
    create_date = models.DateField(auto_now=True)

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = u'主机端口类型'
        verbose_name_plural = u'主机端口类型'


class zhuji_duankou(models.Model):
    leixing_id = models.ForeignKey(leixing,verbose_name="主机端口类型")
    name = models.CharField(max_length=50,verbose_name="主机端口")
    zhuji_duankou_many = models.ManyToManyField("zhuji_ip",verbose_name="主机IP")
    url_address = models.CharField(max_length=255,verbose_name="url地址")
    jiaoben = models.CharField(max_length=255,verbose_name="脚本绝对路径")
    create_date = models.DateField(auto_now=True)
    def __unicode__(self):
        return "%s(%s)" % (self.name,self.leixing_id)

    class Meta:
        verbose_name = u'主机端口'
        verbose_name_plural = u'主机端口'

class zhuji_ip(models.Model):
    ip = models.GenericIPAddressField(unique=True,verbose_name=u'主机IP')
    create_date = models.DateField(auto_now=True)

    def __unicode__(self):
        return "%s" % self.ip

    class Meta:
        verbose_name = u'主机IP'
        verbose_name_plural = u'主机IP'

class task(models.Model):
    task_id = models.CharField(max_length=128,primary_key=True,verbose_name="任务ID")
    title = models.CharField(blank=True,max_length=255,verbose_name="任务标题")
    context = models.TextField(blank=True,verbose_name="任务上下文")
    username = models.CharField(max_length=20,verbose_name="任务用户")
    task_zhuangtai = models.CharField(blank=True,null=True,max_length=10,verbose_name="任务状态")
    task_biaoji = models.CharField(blank=True,max_length=10,verbose_name="任务标记",help_text="""
    标识
      ..1 重启应用任务
      ..2 发版任务
      ..3 回滚任务

    """)
    task_time = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return "%s(%s)" % (self.task_id,self.title)
    class Meta:
        verbose_name = u'任务'
        verbose_name_plural = u'任务'
