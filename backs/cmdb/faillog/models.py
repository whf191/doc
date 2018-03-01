#coding=utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import  User

class shijian_tichuzhe(models.Model):
    user_id = models.ForeignKey(User,help_text="事件提出者,监控人",verbose_name="事件提出者")
    def __unicode__(self):
        return "%s" % self.user_id.first_name
    class Meta:
        verbose_name = '事件提出者'
        verbose_name_plural = '事件提出者'

class shijian_shouliren(models.Model):
    user_id = models.ForeignKey(User,help_text="事件受理人",verbose_name="事件受理人")
    def __unicode__(self):
        return "%s" % self.user_id
    class Meta:
        verbose_name = '事件受理人'
        verbose_name_plural = '事件受理人'
class shijian_chuliren(models.Model):
    user_id = models.ForeignKey(User,help_text="事件处理人",verbose_name="事件处理人")
    def __unicode__(self):
        return "%s" % self.user_id
    class Meta:
        verbose_name = '事件处理人'
        verbose_name_plural = '事件处理人'

class shijian_jibie(models.Model):
    name = models.CharField(max_length=60,choices=(('p0',"高"),('p1',"中"),('p2',"低") )
      ,help_text="""
      事件级别解释：
P0：线上业务相关（主要是指影响交易的事故，比如主站、m站、help无法访问、登录、加入购物车等影响范围大，程度高的事件）
P1：话务系统、邮箱、工作站、erp、crm、IM、内网网络 等影响范围广，程度中的事件
P2：考试系统、金蝶、考勤等程度低的一般事件

      """
                            ,verbose_name="事件级别")


    def __unicode__(self):
        return "%s" % self.name


    class Meta:
        verbose_name = '事件级别'
        verbose_name_plural = '事件级别'



class yingyong_host(models.Model):
    name =  models.CharField(max_length=100,help_text="应用服务器",verbose_name="应用服务器")
    def __unicode__(self):
        return "%s" % self.name
    class Meta:
        verbose_name = '应用服务器'
        verbose_name_plural = '应用服务器'

class didian(models.Model):
    name = models.CharField(max_length=100,help_text="那个地方出的问题",verbose_name="地点")

    def __unicode__(self):
        return "%s" % self.name
    class Meta:
        verbose_name = '地点'
        verbose_name_plural = '地点'
class shijian_yuanyin(models.Model):
    name = models.CharField(max_length=255,help_text="事件原因",verbose_name="事件原因")

    def __unicode__(self):
        return "%s" % self.name


    class Meta:
        verbose_name = '事件原因'
        verbose_name_plural = '事件原因'

class guzhang_biaoxian(models.Model):
    name = models.CharField(max_length=255,help_text="故障表现",verbose_name="故障表现")

    def __unicode__(self):
        return "%s" % self.name


    class Meta:
        verbose_name = '故障表现'
        verbose_name_plural = '故障表现'


class guzhang_jilu(models.Model):
    shijian_riqi = models.DateField(help_text="事件日期",verbose_name="事件日期")
    sj_tichuzhe = models.ForeignKey(shijian_tichuzhe,verbose_name="事件提出者")
    fasheng_shijian = models.TimeField(verbose_name="发生时间")
    gz_biaoxian = models.ForeignKey(guzhang_biaoxian,verbose_name="故障表现")
    sj_shouliren = models.ManyToManyField(shijian_shouliren,verbose_name="事件受理人")
    shouli_shijian = models.DateTimeField(verbose_name="事件受理时间")
    sj_chuliren = models.ManyToManyField(shijian_chuliren,verbose_name="事件处理人")
    huifu_shijian = models.DateTimeField(verbose_name="恢复时间")
    sj_jibie = models.ForeignKey(shijian_jibie,verbose_name="事件级别"
                                 ,help_text="""

      事件级别解释：
P0：线上业务相关（主要是指影响交易的事故，比如主站、m站、help无法访问、登录、加入购物车等影响范围大，程度高的事件）
P1：话务系统、邮箱、工作站、erp、crm、IM、内网网络 等影响范围广，程度中的事件
P2：考试系统、金蝶、考勤等程度低的一般事件

                                 """
                                 )


    yy_host = models.ManyToManyField(yingyong_host,verbose_name="应用服务器")
    host_didian = models.ForeignKey(didian,verbose_name="服务器地点")
    sj_yuanyin = models.ForeignKey(shijian_yuanyin,verbose_name="事件原因")
    sj_chili = models.CharField(max_length=255,verbose_name="处理办法")
    note = models.TextField(verbose_name="备注",blank=True)

    def __unicode__(self):
        return "%s" % self.shijian_riqi

    class Meta:
        verbose_name = '故障记录'
        verbose_name_plural = '故障记录'

