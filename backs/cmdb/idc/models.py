#coding=utf-8
from __future__ import unicode_literals
from django.db import models
from  django.contrib.auth.models import User
# Create your models here.

class idc(models.Model):
    jifang = models.CharField(max_length=100,help_text="机房环境,深圳沙河机房,广州肇庆机房,成都机房",verbose_name="IDC机房",unique=True)
    createdate = models.DateField(auto_now=True)
    def __unicode__(self):
        return "%s" % self.jifang
    class Meta:
        verbose_name = u'IDC'
        verbose_name_plural = u'IDC'

class hosts(models.Model):
    idc_id = models.ForeignKey(idc,help_text="主机归属那个机房",verbose_name="IDC机房")
    hostname = models.CharField(max_length=100,help_text="主机名",verbose_name="主机名",blank=True)
    xitong = models.CharField(max_length=100,help_text="系统",verbose_name="系统",choices=(("linux","linux"),("windows","windows")),default="linux")
    hostip   = models.GenericIPAddressField(verbose_name="主机IP",blank=True,null=True)
    hostport = models.IntegerField(default=22,verbose_name="端口",blank=True,null=True)
    hostuser = models.CharField(max_length=50,help_text="主机用户",verbose_name="主机用户",blank=True)
    hostspassword = models.CharField(max_length=32,help_text="主机密码",verbose_name="主机密码",blank=True)
    node = models.TextField(help_text="备注",verbose_name="备注",blank=True)
    createdate = models.DateField(auto_now=True)
    def __unicode__(self):
        return "%s(%s)" % (self.hostname,self.hostip)
    class Meta:
        verbose_name = u'线上主机信息'
        verbose_name_plural = u'线上主机信息'

class chengduneiwang(models.Model):
    ip = models.CharField(max_length=100,verbose_name="ip",blank=True,null=True)
    guanli = models.CharField(max_length=100,verbose_name="管理员",blank=True,null=True)
    mima = models.CharField(max_length=128,verbose_name="密码",blank=True,null=True)
    beizhu_yonghu = models.CharField(max_length=255,verbose_name="备注-用途",blank=True,null=True)
    chushi_shiyong_riqi = models.CharField(max_length=50,blank=True,null=True)
    zhuyao_shiyongzhe = models.CharField(max_length=100,verbose_name="主要使用者",blank=True,null=True)
    shebeileixing = models.CharField(max_length=100,verbose_name="设备类型",blank=True,null=True)
    guanli_dizhi = models.CharField(max_length=255,verbose_name="管理地址",blank=True,null=True)
    wifi_ssid = models.CharField(max_length=100,verbose_name="wiif_ssid",blank=True,null=True)
    wifi_pwd = models.CharField(max_length=128,verbose_name="wiif_pwd",blank=True,null=True)

    class Meta:
        verbose_name = u'成都内网'
        verbose_name_plural = u'成都内网'
        ordering = ['pk']

class shahexianshangyingyong(models.Model):
    fabanlujing = models.CharField(max_length=255,verbose_name="发版路径",blank=True,null=True)
    fuwuming = models.CharField(max_length=255,verbose_name="服务名",blank=True,null=True)
    rizhilujing = models.CharField(max_length=255,verbose_name="日志路径",blank=True,null=True)
    qidongjiaoben = models.CharField(max_length=255, verbose_name="启动脚本", blank=True, null=True)
    fuwuqi = models.CharField(max_length=255, verbose_name="服务器", blank=True, null=True)
    duankou = models.CharField(max_length=50, verbose_name="端口", blank=True, null=True)
    beizhu = models.CharField(max_length=255, verbose_name="备注", blank=True, null=True)

    class Meta:
        verbose_name = u'线上业务分布'
        verbose_name_plural = u'线上业务分布'
        ordering = ['pk']