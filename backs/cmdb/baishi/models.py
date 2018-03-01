#coding=utf-8
from __future__ import unicode_literals
from django.db import models
from  django.contrib.auth.models import User


class jiazhang(models.Model):
    name = models.CharField(max_length=20,verbose_name="姓名")
    xingbie = models.CharField(choices=(('boy','男'),('girl',"女")),max_length=20,verbose_name="姓别",default="boy",blank=True)
    alias = models.CharField(max_length=20,blank=True,verbose_name="别名")
    tel = models.CharField(max_length=30,verbose_name="电话",unique=True)
    email = models.EmailField(blank=True,verbose_name="邮箱")
    weixin_id = models.CharField(blank=True,verbose_name="微信企业号用户ID",max_length=100)
    Notes= models.TextField(verbose_name="备注",blank=True)
    create_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = u'家长'
        verbose_name_plural = u'家长'


class kaohao(models.Model):
    name = models.IntegerField(verbose_name="考号",unique=True)
    biaoji = models.BooleanField(default=False,help_text="标记是否使用，默认未使用",verbose_name="标记状态",blank=True)
    Notes = models.TextField(verbose_name="备注", blank=True)
    create_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = u'考号'
        verbose_name_plural = u'考号'



class banji(models.Model):
    name = models.CharField(max_length=255,verbose_name="班级",help_text="例子:2016级一班", unique=True)
    laoshi = models.ManyToManyField(User,help_text="班级下绑定那些老师",verbose_name="老师")
    Notes = models.TextField(verbose_name="备注", blank=True)
    create_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = u'班级绑定老师'
        verbose_name_plural = u'班级绑定老师'


class xuesheng(models.Model):
    kaohao_id = models.OneToOneField(kaohao,help_text="学生的考号唯一",verbose_name="考号")
    xuehao = models.IntegerField(verbose_name="学号")
    banji_id = models.ForeignKey(banji,verbose_name="班级",help_text="学生属于那个班级")
    jiazhang_id= models.ManyToManyField(jiazhang,verbose_name="学生绑定家长")

    name = models.CharField(max_length=20,verbose_name="姓名")
    xingbie = models.CharField(choices=(('boy', '男'), ('girl', "女")), max_length=20, verbose_name="性别",default="boy")
    alias = models.CharField(max_length=20, blank=True, verbose_name="别名")
    tel = models.CharField(max_length=20,verbose_name="电话", blank=True)
    email = models.EmailField(blank=True, verbose_name="邮箱")
    weixin_id = models.CharField(blank=True, verbose_name="微信用户ID", max_length=100,help_text="可以不填，预留接口")
    Notes = models.TextField(verbose_name="备注", blank=True)
    create_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = u'学生绑定班级和家长'
        verbose_name_plural = u'学生绑定班级和家长'


class type_chengji(models.Model):
    name = models.CharField(max_length=200,verbose_name="成绩类型",unique=True,help_text="所有班级共享一套成绩类型")
    biaoji = models.BooleanField(default=False,help_text="默认可见,预留接口，不必理会",verbose_name="是否关闭",blank=True)
    Notes = models.TextField(verbose_name="备注", blank=True)
    create_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = u'成绩类型'
        verbose_name_plural = u'成绩类型'


class chengjibiao(models.Model):
    xuesheng_id = models.ForeignKey(xuesheng,verbose_name="学生")
    type_chengji_id = models.ForeignKey(type_chengji,verbose_name="成绩类型")
    yuwen = models.CharField(max_length=20,blank=True,verbose_name="语文")
    shuxue = models.CharField(max_length=20,blank=True, verbose_name="数学")
    yingyu = models.CharField(max_length=20,blank=True, verbose_name="英语")
    zhengzhi = models.CharField(max_length=20,blank=True, verbose_name="政治")
    lishi = models.CharField(max_length=20,blank=True, verbose_name="历史")
    dili = models.CharField(max_length=20,blank=True, verbose_name="地理")
    shengwu = models.CharField(max_length=20,blank=True, verbose_name="生物")
    zongfen = models.CharField(max_length=20,blank=True, verbose_name="总分")
    xiaozongfen = models.CharField(max_length=20, blank=True, verbose_name="小总分")
    nianji_mingci = models.CharField(blank=True, verbose_name="年纪名次",max_length=10)
    banji_mingci = models.CharField(blank=True, verbose_name="班级名次",max_length=10)
    Notes = models.TextField(verbose_name="备注", blank=True)
    create_date = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return "%s" % self.xuesheng_id
    class Meta:
        verbose_name = u'成绩'
        verbose_name_plural = u'成绩'

class piliang_daoru(models.Model):
    name = models.CharField(max_length=90,blank=True,verbose_name="导入名称")
    chengji_leixing = models.ForeignKey(type_chengji,verbose_name="成绩类型",help_text="如果选错成绩类型导入，会多出重复的成绩哦")
    excl_file = models.FileField(upload_to="./update/%Y%m%d",verbose_name="excl表格",help_text="上传的excl必须符合模板规则")
    daoru_biaoshi = models.CharField(max_length=1,verbose_name="导入标识",default="0",help_text=""
    "1为表示已导入，默认0表示未导入",blank=True)
    note = models.TextField(blank=True,verbose_name="备注")
    create_date = models.DateTimeField(auto_now=True,verbose_name="日期")

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = u'成绩批量导入'
        verbose_name_plural = u'成绩批量导入'

class piliang_xuesheng_jiazhang_daoru(models.Model):
    name = models.CharField(max_length=90,blank=True,verbose_name="导入名称")
    banji_leixing = models.ForeignKey(banji,verbose_name="班级类型")
    excl_file = models.FileField(upload_to="./update/%Y%m%d",verbose_name="excl表格",help_text="上传的excl必须符合模板规则")
    daoru_biaoshi = models.CharField(max_length=1,verbose_name="导入标识",default="0",help_text=""
    "1为表示已导入，默认0表示未导入",blank=True)
    note = models.TextField(blank=True,verbose_name="备注")
    create_date = models.DateTimeField(auto_now=True,verbose_name="日期")

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = u'学生家长批量导入'
        verbose_name_plural = u'学生家长批量导入'

