#coding=utf-8
from __future__ import unicode_literals
from  django.contrib.auth.models import User
from django.db import models

class idc(models.Model):
    type = models.CharField(max_length=20,choices=(('开发环境',"开发环境"),('测试环境','测试环境'),('线上环境',"线上环境")),verbose_name="IDC环境",unique=True)
    create_date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return "%s(%s)" % (self.type, self.pk)
    class Meta:
        verbose_name = u'IDC环境'
        verbose_name_plural = u'IDC环境'


class shenqing_vhost(models.Model):
    shenqing_mingzi = models.CharField(max_length=100,help_text=u"申请虚拟主机的名称",verbose_name=u"主机名称")
    type_idc_id = models.ForeignKey(idc,help_text=u"选择一个环境",verbose_name=u"主机环境")
    type_apps = models.CharField(max_length=20,choices=(('mysql','mysql'),('redis','redis'),('mongodb','mongodb'),('zookeeper','zookeeper')),verbose_name=u"应用类型")
    note = models.CharField(max_length=255,blank=True,null=True,help_text=u"填写额外的信息",verbose_name=u"备注")
    shenqing_status = models.CharField(choices=(('1',u'申请提交'),('2',u'申请成功'),('3',u'申请失败'),('4',u'未申请')),default="4",max_length=1,verbose_name=u"申请状态")
    #状态为1为开启，0为删除，逻辑删除标识
    use_flag = models.IntegerField(default=1,verbose_name=u"逻辑删除标识")
    user_id = models.ForeignKey(User,verbose_name=u"用户id")
    create_date = models.DateField(auto_now_add=True,verbose_name=u"创建的时间")
    end_date = models.DateField(verbose_name=u"使用结束时间",help_text=u"长时间用，选择一个长一点的时间吧")

    def __unicode__(self):
        return "%s(%s)->环境:%s" % (self.shenqing_mingzi, self.pk,self.type_idc_id)

    class Meta:
        verbose_name = u'申请虚拟主机'
        verbose_name_plural = u'申请虚拟主机'

class guanli_vhost(models.Model):
    shenqing_vhost_id = models.OneToOneField(shenqing_vhost,verbose_name=u"申请主机的ID")
    vhost_ip = models.OneToOneField("ipaddress_vhost",help_text=u"填写虚拟主机的外部ip地址",verbose_name=u"主机绑定的IP",unique=True)

    class Meta:
        verbose_name = u'管理虚拟主机'
        verbose_name_plural = u'管理虚拟主机'


class ipaddress_vhost(models.Model):
    ip = models.GenericIPAddressField(unique=True)
    is_enable = models.BooleanField(default=False,help_text=u"默认为False，代表可以实用",blank=True)
    create_date = models.DateField(auto_now_add=True, verbose_name=u"创建的时间")
    def __unicode__(self):
        return "%s" %  (self.ip)
    class Meta:
        verbose_name = u"添加虚拟主机IP"
        verbose_name_plural = u'添加虚拟主机IP'