#coding=utf-8
from __future__ import unicode_literals
from django.db import models

#监控部分
class fu_lujing(models.Model):
    alias = models.CharField(max_length=60,help_text="父路径别名",verbose_name="父路径别名")
    name = models.CharField(max_length=255,help_text="父路径",verbose_name="父路径")
    create_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s" % self.alias

    class Meta:
        verbose_name = '父路径'
        verbose_name_plural = '父路径'


class zi_lujing(models.Model):
    alias = models.CharField(max_length=60,help_text="子路径别名",verbose_name="子路径别名")
    fu_lujing_id = models.ForeignKey(fu_lujing,verbose_name="父路径")
    name = models.CharField(max_length=255,help_text="子路径的目的对应排除",verbose_name="子路径")
    create_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s" % self.alias

    class Meta:
        verbose_name = '子路径'
        verbose_name_plural = '子路径'


#记录部分

class didian(models.Model):
    alias = models.CharField(max_length=60,help_text="地方别名",verbose_name="地方别名")
    name = models.CharField(max_length=60,help_text="地方",verbose_name="地方")

    def __unicode__(self):
        return "%s" % self.alias

    class Meta:
        verbose_name = '地方'
        verbose_name_plural = '地方'

class zhuangtai(models.Model):
    alias = models.CharField(max_length=60, help_text="状态别名", verbose_name="状态别名")
    name = models.CharField(max_length=120,help_text="状态指增删改查等...")

    def __unicode__(self):
        return "%s" % self.alias

    class Meta:
        verbose_name = '状态'
        verbose_name_plural = '状态'

class jilu(models.Model):
    didian_id = models.ForeignKey(didian,verbose_name="地点")
    host = models.CharField(max_length=60,help_text="线上主机名",verbose_name="线上主机名")
    neirong = models.CharField(max_length=255,verbose_name="路径信息")
    zhuangtai_id = models.ForeignKey(zhuangtai,verbose_name="状态")

    def __unicode__(self):
        return "%s(%s)(%s)" % (self.host,self.neirong,self.zhuangtai_id)

    class Meta:
        verbose_name = '记录'
        verbose_name_plural = '记录'