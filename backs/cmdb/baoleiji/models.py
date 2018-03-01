#coding=utf-8
from __future__ import unicode_literals
from django.db import models
from  django.contrib.auth.models import User
# Create your models here.

class idc(models.Model):
    jifang = models.CharField(max_length=100,help_text="机房环境,深圳机房，成都机房",verbose_name="IDC机房",unique=True)
    createdate = models.DateField(auto_now=True)
    def __unicode__(self):
        return "%s" % self.jifang
    class Meta:
        verbose_name = u'IDC'
        verbose_name_plural = u'IDC'

class hosts(models.Model):
    idc_id = models.ForeignKey(idc,help_text="主机归属那个机房",verbose_name="IDC机房")
    hostname = models.CharField(max_length=100,help_text="主机名",verbose_name="主机名")
    hostip   = models.GenericIPAddressField(unique=True,help_text="主机ip,必须唯一",verbose_name="主机IP")
    hostport = models.IntegerField(default=22,verbose_name="SSH端口")
    hostuser = models.CharField(max_length=50,help_text="主机用户",verbose_name="主机用户")
    hostspassword = models.CharField(max_length=32,help_text="主机密码",verbose_name="主机密码")
    createdate = models.DateField(auto_now=True)
    def __unicode__(self):
        return "%s(%s)" % (self.hostname,self.hostip)
    class Meta:
        verbose_name = u'远程主机'
        verbose_name_plural = u'远程主机'

class mulu_sfile_dfile(models.Model):
    bieming = models.CharField(max_length=255,verbose_name="别名")
    hosts_id = models.ForeignKey(hosts,verbose_name="绑定主机")
    mulu = models.CharField(max_length=255,verbose_name="目标目录",help_text="此处是目标目录")
    sfile = models.CharField(max_length=255,verbose_name="源文件")
    dfile = models.CharField(max_length=255,verbose_name="目标文件")
    createuser = models.ForeignKey(User,verbose_name="绑定用户")
    createdate = models.DateField(auto_now=True)
    def __unicode__(self):
        return self.bieming
    class Meta:
        verbose_name = "主机目录文件"
        verbose_name_plural = "主机目录文件"

class gongong_shell(models.Model):
    bieming = models.CharField(max_length=255,verbose_name="别名")
    mulu = models.CharField(max_length=255,verbose_name="目标目录",help_text="此处是目标目录")
    sfile = models.CharField(max_length=255,verbose_name="源文件",unique=True)
    dfile = models.CharField(max_length=255,verbose_name="目标文件")
    createdate = models.DateField(auto_now=True)
    def __unicode__(self):
        return self.bieming
    class Meta:
        verbose_name = "公共shell目录文件"
        verbose_name_plural = "公共shell目录文件"

class bind_users_hosts(models.Model):
    user_alias = models.CharField(max_length=50,blank=True,help_text="用户别名",verbose_name="用户别名")
    user_id = models.OneToOneField(User,help_text="对应的真实用户",verbose_name="真实用户")
    hosts_id = models.ManyToManyField(hosts,help_text="用户和主机的多对多关系",verbose_name="用户主机")
    createdate = models.DateField(auto_now=True)
    def __unicode__(self):
        return "%s(%s)" % (self.user_alias,self.user_id)
    class Meta:
        verbose_name = "绑定用户和主机"
        verbose_name_plural = "绑定用户和主机"

class shenji(models.Model):
    username = models.CharField(max_length=50,help_text="记录用户",verbose_name="用户")
    hostip = models.CharField(max_length=50,help_text="记录操作的主机ip",verbose_name="主机IP")
    host_cmd = models.CharField(max_length=255,help_text="记录操作的指令",verbose_name="指令")
    createdate = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return "%s" % self.host_cmd
    class Meta:
        verbose_name = "审计信息"
        verbose_name_plural = "审计信息"
