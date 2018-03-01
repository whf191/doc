#coding=utf-8
#from __future__ import unicode_literals

from django.db import models
from  django.contrib.auth.models import User
from django.utils import timezone

#主容器类型，用于申请容器使用
class type_rongqi(models.Model):
    rongqi_name = models.CharField(max_length=100,verbose_name=u"容器别名")
    rongqi_type = models.CharField(max_length=100,verbose_name=u"主容器类型")
    create_date = models.DateField(auto_now_add=True,verbose_name=u"创建的时间")
    def __unicode__(self):
        return "%s(%s)" % (self.rongqi_name,self.rongqi_type)

    class Meta:
        verbose_name = u'主容器类型'
        verbose_name_plural = u'主容器类型'



#申请容器
class shenqing_rongqi(models.Model):
    shenqing_mingzi = models.CharField(max_length=100,help_text=u"申请容器的名称",verbose_name=u"申请容器名称")
    type_rongqi_id = models.ForeignKey(type_rongqi,help_text=u"选择一个父容器",verbose_name=u"父容器")
    shenqing_status = models.CharField(choices=(('1','申请提交'),('2','申请成功'),('3','申请失败'),('4','未申请')),default="4",max_length=1,verbose_name=u"申请状态")
    #状态为1为开启，0为删除，逻辑删除标识
    use_flag = models.IntegerField(default=1,verbose_name=u"逻辑删除标识")
    user_id = models.ForeignKey(User,verbose_name=u"用户id")
    create_date = models.DateField(auto_now_add=True,verbose_name=u"创建的时间")
    end_date = models.DateField(verbose_name=u"容器使用结束时间",help_text=u"此选项必填")

    def __unicode__(self):
        return "%s" % self.shenqing_mingzi

    class Meta:
        verbose_name = u'申请容器'
        verbose_name_plural = u'申请容器'


# #申请需要开放的端口 ---采用docker和物理主机桥接模式，放弃此方法
# class duankou_rongqi(models.Model):
#     rongqi_duankou = models.IntegerField(verbose_name=u"容器外部端口")
#     shenqing_rongqi_id = models.ForeignKey(shenqing_rongqi,verbose_name=u"申请容器的ID")
#     create_date = models.DateField(auto_now_add=True,verbose_name=u"创建的时间")
#     def __unicode__(self):
#         return "%s" % self.pk
#     class Meta:
#         verbose_name = u'绑定容器外部端口'
#         verbose_name_plural = u'绑定容器外部端口'


#管理容器

class guanli_rongqi(models.Model):
    shenqing_rongqi_id = models.OneToOneField(shenqing_rongqi,verbose_name=u"申请容器的名称")
    rongqi_ip = models.OneToOneField("ipaddress_rongqi",help_text=u"填写容器的外部ip地址",verbose_name=u"容器绑定的IP",unique=True)
    rongqi_id = models.CharField(max_length=100,verbose_name=u"生成容器ID",unique=True)
    create_date = models.DateField(auto_now_add=True,verbose_name=u"创建的时间")
    external_directory = models.CharField(max_length=30,blank=True,null=True,verbose_name=u"外部挂载盘",help_text=u"真实服务器的存放路径")

    def __unicode__(self):
        return "%s" % self.shenqing_rongqi_id


    class Meta:
        verbose_name = u'管理容器'
        verbose_name_plural = u'管理容器'


#容器父ip
class pipaddress_rongqi(models.Model):
    ip_name = models.CharField(max_length=50,verbose_name=u"Docker宿主机名")
    ip = models.GenericIPAddressField(unique=True,verbose_name=u'Docker宿主机IP')
    password = models.CharField(max_length=20,verbose_name=u"宿主机密码",blank=True,null=True)
    geteway = models.GenericIPAddressField(verbose_name=u'网关')
    create_date = models.DateField(auto_now_add=True, verbose_name=u"创建的时间")
    def __unicode__(self):
        return "%s(%s)" %  (self.ip_name,self.ip)
    class Meta:
        verbose_name = u'Docker宿主机'
        verbose_name_plural = u'Docker宿主机'

#容器IP
class ipaddress_rongqi(models.Model):
    pipaddress_rongqi_id = models.ForeignKey(pipaddress_rongqi,verbose_name="Docker宿主机")
    ip_name = models.CharField(max_length=50,choices=(('1',"研发部门"),("2",'架构部门'),("3","测试部门")),help_text=u"部门名称,1->研发部门 2->架构部门 3->测试部门")
    ip = models.GenericIPAddressField(unique=True)
    is_enable = models.BooleanField(default=False,help_text=u"默认关闭",blank=True)
    create_date = models.DateField(auto_now_add=True, verbose_name=u"创建的时间")
    def __unicode__(self):
        return "%s(%s)" %  (self.ip,self.pipaddress_rongqi_id)
    class Meta:
        verbose_name = u"添加容器IP"
        verbose_name_plural = u'添加容器IP'


#web创建容器模型,这个地方有个坑哦，跟views视图的create_rongqi名字重名了
class create_rongqi(models.Model):
    shenqing_id = models.IntegerField(help_text=u"输入订单ID",verbose_name=u"申请ID")
    ipaddress_rongqi_id = models.ForeignKey(ipaddress_rongqi,verbose_name=u"绑定IP")
    create_date =  models.DateTimeField(auto_now=True,verbose_name=u"创建时间")
    note = models.CharField(max_length=255,blank=True,null=True,verbose_name=u"备注")
    iscreate = models.BooleanField(default=False,help_text=u"是否被创建",blank=True)
    def __unicode__(self):
        return "%s(%s)" % (self.shenqing_id,self.ipaddress_rongqi_id)

    class Meta:
        verbose_name = u"创建容器"
        verbose_name_plural = u'创建容器'