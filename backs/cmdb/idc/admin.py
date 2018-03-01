from django.contrib import admin
from django.forms import ModelForm
from .models import  *
from suit_redactor.widgets import RedactorWidget
from suit_ckeditor.widgets import CKEditorWidget
# Register your models here.


class PageForm(ModelForm):
    class Meta:
        widgets = {
           # 'node':CKEditorWidget(editor_options={'startupFocus':True})
            'node': RedactorWidget(editor_options={'lang': 'en'})

        }



class hosts_zdy(admin.ModelAdmin):
    form = PageForm
    list_display = ('hostname','hostspassword','xitong','hostip','hostport')
    search_fields = ['hostip','hostname']
    list_filter = ('idc_id',)

class chengduneiwang_zdy(admin.ModelAdmin):
    list_display = ("ip","guanli","mima","wifi_ssid","wifi_pwd")
    search_fields = ("ip","guanli","mima","wifi_ssid","wifi_pwd","shebeileixing","guanli_dizhi","beizhu_yonghu","zhuyao_shiyongzhe")
    list_filter = ('shebeileixing',)
class shahexianshangyingyong_zdy(admin.ModelAdmin):
    list_display = ("fabanlujing","fuwuming","duankou","rizhilujing","qidongjiaoben","beizhu","fuwuqi")
    search_fields = ("fabanlujing","fuwuming","duankou")
    list_filter = ('duankou','fuwuming')


admin.site.register(idc)

admin.site.register(hosts,hosts_zdy)
admin.site.register(chengduneiwang,chengduneiwang_zdy)
admin.site.register(shahexianshangyingyong,shahexianshangyingyong_zdy)
