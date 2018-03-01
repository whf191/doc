#coding=utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import datetime,time

def get_date():
    s = datetime.date.today()
    today = []
    today.append(s.year)
    today.append(s.month)
    today.append(s.day)
    today = map(str,today)
    today = "_".join(today)
    return today
def sjc():
    s = datetime.datetime.today()
    today = []
    today.append(s.year)
    today.append(s.month)
    today.append(s.day)
    today.append(s.hour)
    today.append(s.minute)
    today.append(s.second)
    today.append(s.microsecond)
    today = map(str, today)
    today = "".join(today)
    return today

# Create your models here.

#收件人邮箱
class  recipient_list_email(models.Model):
    user_id = models.OneToOneField(User,help_text="关联收件人邮箱",verbose_name="用户")
    create_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s" % self.user_id


    class Meta:
        verbose_name = u'程序收件人邮箱'
        verbose_name_plural = u'程序收件人邮箱'

#运维收件人邮箱，用途是发版人审核通过的通知

class yunwei_recipient_list_email(models.Model):
    user_id = models.OneToOneField(User,help_text="关联运维收件人邮箱",verbose_name="用户")
    create_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s" % self.user_id


    class Meta:
        verbose_name = u'运维收件人邮箱'
        verbose_name_plural = u'运维收件人邮箱'





class extend_user_permissions(models.Model):
    user_id=models.OneToOneField(User,help_text="扩展用户权限",verbose_name="扩展用户权限")
    permissions = models.CharField(max_length=10,choices=(("1","发版用户"),('2','发版审核用户')),help_text=
                                 "标识用户的发版权限" ,verbose_name="用户权限"
                                   )

    faban_types_many_id = models.ManyToManyField("faban_types",verbose_name="关联那些发版类型")

    recipient_list_email_id = models.ManyToManyField(recipient_list_email,verbose_name="通知程序那些收件人")

    yunwei_recipient_list_email_id = models.ManyToManyField(yunwei_recipient_list_email,verbose_name="通知运维那些收件人")
    create_date = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return "%s" % self.user_id


    class Meta:
        verbose_name = u'扩展用户权限'
        verbose_name_plural = u'扩展用户权限'


class fu_faban_type(models.Model):
    name = models.CharField(max_length=30,help_text="发版类型",verbose_name="发版类型")
    create_date = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return "%s" % self.name


    class Meta:
        verbose_name = u'发版类型'
        verbose_name_plural = u'发版类型'

class faban_types(models.Model):
    """
    开动大脑，此处可以扩展，发版按钮,比如脚本存放路径...
    """
    fu_faban_type_ids = models.ForeignKey(fu_faban_type,verbose_name="父类型")
    name = models.CharField(max_length=30,help_text="发版应用",verbose_name="发版应用")
    wu_id = models.CharField(max_length=1,help_text="特殊字段,只用于没有权限的用户,只能有一个字段和它匹配",default="0",blank=True)
    jiaoben = models.CharField(max_length=100,help_text="应用对应的脚本",verbose_name="发版脚本")
    create_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s" % self.name


    class Meta:
        verbose_name = u'发版应用'
        verbose_name_plural = u'发版应用'


class faban_upload(models.Model):
    faban_types_id = models.ForeignKey(faban_types,help_text="用户拥有的发版类型",verbose_name="发版类型")
    upfile = models.FileField(upload_to="./update/%Y%m%d" ,verbose_name="附件",help_text="注意:上传的附件，必须和发版类型一致，"
                                                                                "不能混合其它类型 ,上传的附件不要有中文和特殊符号")
    shenqing = models.CharField(max_length=1,blank=True,null=True,default="0",help_text="""
        值为0，表示没有申请
        值为1，表示申请
        ..2,  已确认
        ..3, 已发版
        ..4, 已回滚

    """)

    faban_user = models.ForeignKey(User,help_text="""
    绑定发版用户
    """,verbose_name="发版用户")


    create_date = models.DateTimeField(auto_now=True)

    shijiancuo = models.CharField(max_length=30,default="1",blank=True)
    note = models.TextField(blank=True,null=True,help_text="附加备注信息",verbose_name="备注")
    shenhe = models.CharField(max_length=11,default="0",help_text="发版完后的审核按钮",verbose_name="审核按钮",blank=True)

    def __unicode__(self):
        return "%s(%s)" % (self.pk,"发版任务")

    class Meta:
        verbose_name = u'发版任务'
        verbose_name_plural = u'发版任务'

##############
"""
架构组新发版系统接入
"""
class jgz_faban_php(models.Model):
    faban_leixing = models.CharField(max_length=255,verbose_name="架构组传过来的发版类型")
    url_zip = models.URLField(verbose_name="url下载路径")
    url_zip_md5 = models.CharField(max_length=255,verbose_name="url_zip的md5")
    faban_id = models.CharField(max_length=255,verbose_name="传过来的ID")
    state = models.CharField(max_length=1,verbose_name="发版状态，1是正常 3是正常已发")
    create_date = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = u'架构组新发版'
        verbose_name_plural = u'架构组新发版'


class jgz_huigun_php(models.Model):
    faban_id = models.CharField(max_length=255,verbose_name="回滚传过来的ID")
    state  = models.CharField(max_length=1,verbose_name="回滚状态,2是回滚，4是回滚已发")
    create_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u'架构组回滚发版'
        verbose_name_plural = u'架构组回滚发版'

class jgz_renwu(models.Model):
    faban_id = models.CharField(max_length=255,verbose_name="传过来的ID")
    state = models.CharField(max_length=1, verbose_name="状态,1是正常发版，2是回滚")
    jilu_log = models.CharField(max_length=255,verbose_name="日志记录文件")
    create_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u'架构组任务记录'
        verbose_name_plural = u'架构组任务记录'

