#coding=utf-8
from __future__ import unicode_literals
from  django.contrib.auth.models import User
from django.db import models
import datetime
class leixing(models.Model):
    name = models.CharField(max_length=255,help_text="工单的类型",verbose_name="工单类型")
    create_date = models.DateTimeField(auto_now=True, verbose_name=u"创建时间")
    def __unicode__(self):
        return "%s" % self.name
    class Meta:
        verbose_name = u'工单类型'
        verbose_name_plural = u'工单类型'

class shijian(models.Model):
    leixing_id = models.ForeignKey(leixing,verbose_name="工单类型")
    fujian = models.FileField(upload_to="./update/",blank=True,verbose_name="附件")
    create_date = models.DateTimeField(auto_now=True, verbose_name=u"创建时间")
    create_end = models.DateField(blank=True,verbose_name="结束时间",help_text="根据情况,选填")
    beizhu = models.TextField(blank=True,verbose_name="备注")
    user_id = models.ForeignKey(User, verbose_name=u"用户id")
    is_shenqing = models.CharField(default='0',max_length=50,choices=(('0','未申请'),('1','申请提交'),('2','已处理')),verbose_name=u"申请状态")
    is_chuli = models.BooleanField(default=False,verbose_name="处理状态")
    def __unicode__(self):
        return "%s" % self.leixing_id
    class Meta:
        verbose_name = u'工单申请'
        verbose_name_plural = u'工单申请'

