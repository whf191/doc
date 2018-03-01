# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class idc(models.Model):
    name = models.CharField(max_length=255, verbose_name="机房")

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = '机房'
        verbose_name_plural = '机房'

class dockerimages(models.Model):
    alias = models.CharField(max_length=255, verbose_name="docker镜像别名")
    name = models.CharField(verbose_name="docker镜像",max_length=255)
    def __unicode__(self):
        return "%s" % self.alias

    class Meta:
        verbose_name = 'docker镜像'
        verbose_name_plural = 'docker镜像'

class dockerhost(models.Model):
    idc_id = models.ForeignKey(idc)
    name = models.CharField(max_length=255, verbose_name="docker主机")
    ip = models.GenericIPAddressField(verbose_name="docker宿主机ip")
    mask = models.CharField(max_length=255, default=22, blank=True, null=True, verbose_name="掩码")
    gateway = models.GenericIPAddressField(verbose_name="网关")
    docker_username = models.CharField(max_length=255,blank=True,verbose_name="docker_用户名")
    docker_password = models.CharField(max_length=255,blank=True,verbose_name="docker_密码")
    pname = models.CharField(max_length=255, blank=True, verbose_name="docker上层物理机")
    pip = models.GenericIPAddressField(verbose_name="docker上层物理机ip")
    username = models.CharField(max_length=255,blank=True,verbose_name="docker上层用户名")
    password = models.CharField(max_length=255,blank=True,verbose_name="docker上层密码")
    create_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s/%s(%s)/%s(%s)" % (self.idc_id,self.name,self.ip,self.pname,self.pip)

    class Meta:
        verbose_name = 'docker主机'
        verbose_name_plural = 'docker主机'

class containerip(models.Model):
    ip = models.GenericIPAddressField(verbose_name="docker主机ip")
    note = models.CharField(max_length=255,blank=True, verbose_name="备注")
    active = models.BooleanField(default=False,verbose_name="激活",help_text="默认IP未使用")
    create_date = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return "%s/%s/%s" % (self.ip,self.note,self.active)

    class Meta:
        verbose_name = '容器IP'
        verbose_name_plural = '容器IP'

class apptype(models.Model):
    name = models.CharField(max_length=255, verbose_name="应用")
    note = models.CharField(max_length=255, blank=True, verbose_name="备注")
    create_date = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return "%s/%s" % (self.name,self.note)

    class Meta:
        verbose_name = '应用类型'
        verbose_name_plural = '应用类型'

class registerscript(models.Model):
    name = models.CharField(max_length=255, verbose_name="脚本",unique=True)
    shell = models.TextField(verbose_name="shell",blank=True)
    create_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = '注册脚本'
        verbose_name_plural = '注册脚本'

class managecontainer(models.Model):
    alias = models.CharField(max_length=255,verbose_name="容器的别名",blank=True,null=True,help_text="程序自动生成，不需要填写.格式:名称_容器IP_开放端口")
    openport = models.CharField(max_length=255,verbose_name="开放的端口",blank=True,null=True)
    dockerhost_id = models.ForeignKey(dockerhost,verbose_name="docker主机")
    dockerimages_id = models.ForeignKey(dockerimages,verbose_name="docker镜像")
    containerip_id = models.ForeignKey(containerip,verbose_name="容器IP")
    container_username = models.CharField(max_length=255,default="root",blank=True,null=True,verbose_name="容器用户名")
    container_password = models.CharField(max_length=255,default="123456",blank=True,null=True,verbose_name="容器密码")
    apptype_id = models.ForeignKey(apptype,verbose_name="应用类型")
    registerscript_id = models.ForeignKey(registerscript,verbose_name="注册脚本")
    state1 = models.CharField(max_length=1,choices=(('1','未确定配置'),('2','配置确定'),('3','容器已创建'),('4','容器创建失败')),default='1',verbose_name="容器创建状态")
    extensions_directory = models.CharField(max_length=255,blank=True,verbose_name="外部挂载目录",help_text="命名格式为dir_id_ip")
    container_id = models.CharField(max_length=255,blank=True,verbose_name="容器ID")
    create_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s" % self.alias

    class Meta:
        verbose_name = '管理容器'
        verbose_name_plural = '管理容器'
