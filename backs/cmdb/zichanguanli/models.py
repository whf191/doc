#coding=utf-8
from __future__ import unicode_literals

from django.db import models

class shebei_leixing(models.Model):
    name = models.CharField(max_length=100,help_text="设备类型",verbose_name="设备类型")
    create_date = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return "%s" % self.name
    class Meta:
        verbose_name = u'设备类型'
        verbose_name_plural = u'设备类型'


class caozuo_leixing(models.Model):
    name = models.CharField(max_length=100,help_text="操作类型",verbose_name="操作类型")
    create_date = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return "%s" % self.name
    class Meta:
        verbose_name = u'操作类型'
        verbose_name_plural = u'操作类型'

class bumen(models.Model):
    name = models.CharField(max_length=100,help_text="部门",verbose_name="部门")
    create_date = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return "%s" % self.name
    class Meta:
        verbose_name = u'部门'
        verbose_name_plural = u'部门'

class changku(models.Model):
    shebei_leixing_id = models.ForeignKey(shebei_leixing,verbose_name="设备类型")
    caozuo_lexing_id = models.ForeignKey(caozuo_leixing,verbose_name="操作类型")


    name = models.CharField(max_length=255,blank=True,help_text="设备名称",verbose_name="设备名称")
    xuliehao = models.CharField(max_length=255, blank=True, help_text="设备序列号", verbose_name="设备序列号")
    zhuji_name = models.CharField(max_length=255, blank=True, help_text="主机名", verbose_name="主机名")
    ip_address = models.CharField(max_length=255, blank=True, help_text="IP地址", verbose_name="IP地址")
    cpu =  models.CharField(max_length=255, blank=True, help_text="CPU", verbose_name="CPU")
    neicun = models.CharField(max_length=255, blank=True, help_text="内存", verbose_name="内存")
    xitong =  models.CharField(max_length=255, blank=True, help_text="系统", verbose_name="系统")
    zhuban = models.CharField(max_length=255, blank=True, help_text="主板", verbose_name="主板")
    zhenlieka = models.CharField(max_length=255, blank=True, help_text="阵列卡", verbose_name="阵列卡")
    yingpan = models.CharField(max_length=255, blank=True, help_text="硬盘", verbose_name="硬盘")
    caigou_riqi = models.DateField(max_length=255, blank=True,null=True, help_text="采购日期", verbose_name="采购日期")
    caigou_shuliang = models.CharField(max_length=255, blank=True, help_text="采购数量", verbose_name="采购数量")

    bumen_id = models.ForeignKey(bumen,verbose_name="部门")
    lingyongren = models.CharField(max_length=255, blank=True, help_text="领用人", verbose_name="领用人")
    lingyong_riq1  = models.DateField(max_length=255, blank=True, null=True,help_text="领用日期", verbose_name="领用日期")
    guihuan_riq = models.DateField(max_length=255, blank=True, null=True,help_text="归还日期", verbose_name="归还日期")
    beizhu = models.TextField(blank=True,help_text="备注",verbose_name="备注")
    create_date = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = u'设备仓库'
        verbose_name_plural = u'设备仓库'

class feiyong_leixing(models.Model):
    name = models.CharField(max_length=255,help_text="费用名称",verbose_name="费用名称")
    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = u'费用类型'
        verbose_name_plural = u'费用类型'

class fufei_fangshi(models.Model):
    name = models.CharField(max_length=255,help_text="付费方式",verbose_name="付费方式")
    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = u'付费方式'
        verbose_name_plural = u'付费方式'


class qingkuan_mingxi(models.Model):
    feiyong_leixing_id = models.ForeignKey(feiyong_leixing,verbose_name="费用类型")
    name = models.CharField(max_length=255,verbose_name="请款名称",blank=True)
    zhifu_jine_fanwei = models.CharField(max_length=255,verbose_name="支付金额范围",blank=True)
    fufei_fangshi_id = models.ForeignKey(fufei_fangshi,verbose_name="付费方式",blank=True)
    shifou_qianding_hetong = models.CharField(max_length=255,verbose_name="合同到期时间",blank=True)
    hanshui_danjia = models.CharField(max_length=255, verbose_name="含税单价",blank=True)
    shuilv = models.CharField(max_length=255, verbose_name="税率", blank=True)
    jiage_danwei = models.CharField(max_length=255, verbose_name="价格单位", blank=True)
    shuliang = models.CharField(max_length=255, verbose_name="数量", blank=True)
    jiliang_danwei = models.CharField(max_length=255, verbose_name="计量单位", blank=True)
    hanshui_heji = models.CharField(max_length=255, verbose_name="含税合计", blank=True)
    guishu_bumen = models.CharField(max_length=255, verbose_name="归属部门", blank=True)
    fapiao_leixing = models.CharField(max_length=255, verbose_name="发票类型", blank=True)
    yongtu = models.CharField(max_length=255,verbose_name="用途",blank=True)
    note = models.TextField(verbose_name="备注",blank=True)


    def __unicode__(self):
        return "%s" % self.name


    class Meta:
        verbose_name = u'请款明细'
        verbose_name_plural = u'请款明细'

class guishu_bumen(models.Model):
    name =  models.CharField(max_length=255,verbose_name="最终归属部门")
    create_date = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = u'最终归属部门'
        verbose_name_plural = u'最终归属部门'


class zuzhuang_taishi_diannao(models.Model):
    name = models.CharField(max_length=255,verbose_name="资产名称")
    xinghao = models.CharField(max_length=255,verbose_name="资产型号",blank=True)
    jixing_fenlei = models.CharField(max_length=255,verbose_name="机型分类",blank=True)
    zichan_bianma = models.CharField(max_length=255,verbose_name="资产编码",blank=True)
    zichan_shiyongzhe = models.CharField(max_length=255,verbose_name="资产使用者",blank=True)
    zichan_yuanguishubumen = models.ForeignKey(bumen,verbose_name="资产原归属部门")
    zichan_zuizhongguishubumen= models.ForeignKey(guishu_bumen,verbose_name="资产最终归属部门")
    create_date = models.DateTimeField(auto_now=True,verbose_name="创建时间")

    def __unicode__(self):
        return "%s" % self.name


    class Meta:
        verbose_name = u'组装台式电脑'
        verbose_name_plural = u'组装台式电脑'


