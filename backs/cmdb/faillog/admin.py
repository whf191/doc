#coding=utf-8
from __future__ import unicode_literals
from django.contrib import admin
from .models import  *
from django.forms import ModelForm
from suit.widgets import SuitDateWidget, SuitTimeWidget, SuitSplitDateTimeWidget
class zdy_riqi(ModelForm):
    class Meta:
        widgets = {
            'shijian_riqi':SuitDateWidget,
            'fasheng_shijian':SuitTimeWidget,
            'shouli_shijian':SuitSplitDateTimeWidget,
            'huifu_shijian':SuitSplitDateTimeWidget
          }



class zdy_guzhang_jilu(admin.ModelAdmin):
    form = zdy_riqi
    filter_horizontal = ('sj_shouliren','sj_chuliren','yy_host')
    raw_id_fields = ('gz_biaoxian','sj_yuanyin')
    #search_fields = ['shijian_riqi','gz_biaoxian']

    list_filter = ('host_didian','sj_jibie')
    fieldsets = (
        ('事件发生段',{'fields':('shijian_riqi','sj_tichuzhe','fasheng_shijian','gz_biaoxian')}),
        ('受理事件段',{'fields':('sj_shouliren','shouli_shijian')}),
        ('事件处理段', {'fields': ('sj_chuliren', 'huifu_shijian','sj_jibie','yy_host'
            ,'host_didian','sj_yuanyin','sj_chili')}
         ),
        ('备注',{'fields':('note',)}) )

    list_display = ('shijian_riqi', 'sj_tichuzhe', 'fasheng_shijian',
                    'gz_biaoxian','huifu_shijian','sj_jibie',
                    'sj_yuanyin')


admin.site.register(shijian_tichuzhe)
admin.site.register(shijian_shouliren)
admin.site.register(shijian_chuliren)
admin.site.register(shijian_jibie)
admin.site.register(yingyong_host)
admin.site.register(didian)
admin.site.register(shijian_yuanyin)
admin.site.register(guzhang_biaoxian)
admin.site.register(guzhang_jilu,zdy_guzhang_jilu)



