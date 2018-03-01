#coding=utf-8
from  __future__ import unicode_literals
from django.contrib import admin
from .models import *
from django.forms import ModelForm
# Register your models here.
from suit.widgets import  SuitDateWidget, SuitTimeWidget, SuitSplitDateTimeWidget

class PageForm2(ModelForm):
    class Meta:
        widgets = {
           # 'node':CKEditorWidget(editor_options={'startupFocus':True})
            #'beizhu': RedactorWidget(editor_options={'lang': 'en'}),
            'caigou_riqi': SuitDateWidget,
            'lingyong_riq1': SuitDateWidget,
            'guihuan_riq': SuitDateWidget
        }

class zdy_changku(admin.ModelAdmin):
    form = PageForm2
    search_fields = ['lingyongren','name']
    list_filter = ('shebei_leixing_id','caozuo_lexing_id','bumen_id')
    list_display = ('shebei_leixing_id','caozuo_lexing_id','name','xuliehao','ip_address','caigou_riqi','bumen_id','lingyongren','lingyong_riq1','guihuan_riq')
    #fields = (('shebei_leixing_id','caozuo_lexing_id'),'name')
    fieldsets = (
        ('设备类型选择',{'fields':(('shebei_leixing_id','caozuo_lexing_id'),)}),
        ('设备参数',{'fields':('name','xuliehao','zhuji_name','ip_address',
        'cpu','neicun','xitong','zhuban','zhenlieka','yingpan','caigou_riqi',
        'caigou_shuliang')}),
        ('部门借用', {'fields': ('bumen_id', 'lingyongren','lingyong_riq1','guihuan_riq'
            ,'beizhu')})


    )


class zdy_qingkuan_mingxi(admin.ModelAdmin):
    list_display = ('feiyong_leixing_id','name','zhifu_jine_fanwei','fufei_fangshi_id','shifou_qianding_hetong')
    raw_id_fields = ('feiyong_leixing_id','fufei_fangshi_id')

class zdy_zuzhuang_taishi_diannao(admin.ModelAdmin):
    list_display = ('name','xinghao','jixing_fenlei','zichan_bianma','zichan_shiyongzhe','zichan_yuanguishubumen',
                    'zichan_zuizhongguishubumen','create_date')
    list_filter = ['zichan_yuanguishubumen','zichan_zuizhongguishubumen']
    search_fields = ['xinghao', 'name','jixing_fenlei','zichan_bianma','zichan_shiyongzhe']

admin.site.register(shebei_leixing)
admin.site.register(caozuo_leixing)
admin.site.register(changku,zdy_changku)
admin.site.register(bumen)
admin.site.register(feiyong_leixing)
admin.site.register(fufei_fangshi)
admin.site.register(qingkuan_mingxi,zdy_qingkuan_mingxi)
admin.site.register(guishu_bumen,)
admin.site.register(zuzhuang_taishi_diannao,zdy_zuzhuang_taishi_diannao)
