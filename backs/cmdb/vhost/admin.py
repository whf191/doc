#coding=utf-8
from django.contrib import admin
from django.forms import  ModelForm
from suit.widgets import  SuitDateWidget, SuitTimeWidget, SuitSplitDateTimeWidget
from models import  *
import time
# Register your models here.

class shenqing_vhost_form(ModelForm):
    class Meta:
        widgets = {
            'end_date':SuitDateWidget
          }

class shenqing_vhost_zdy(admin.ModelAdmin):
    form = shenqing_vhost_form
    save_on_top = True
    list_display = ('pk_zdy','shenqing_mingzi','type_idc_id','type_apps','note','shenqing_status','create_date','end_date','user_id','shenqing_tijiao')
    fields = ('shenqing_mingzi','type_idc_id','type_apps','note','user_id','end_date')

    #自定义申请主键ID的字段
    def pk_zdy(self,obj):
        return obj.pk
    pk_zdy.short_description = "主机ID"

    #普通用户只能看到自己的申请列表
    def get_queryset(self, request):
        qs = super(shenqing_vhost_zdy, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        get_userid = shenqing_vhost.objects.filter(user_id=request.user.id)
        return get_userid

    #重写外键方法
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if not request.user.is_superuser:
            if db_field.name == "user_id":
                kwargs['queryset'] = User.objects.filter(pk=request.user.id)
        return super(shenqing_vhost_zdy,self).formfield_for_foreignkey(db_field, request, **kwargs)

    #干掉普通用的actions 操作
    def get_actions(self, request):
        actions = super(shenqing_vhost_zdy, self).get_actions(request)
        if request.user.is_superuser:
            return  actions
        del actions['delete_selected']
        return  actions

    #自定义申请提交字段的方法
    def shenqing_tijiao(self,obj):
        if  obj.shenqing_status == "4":
            return '<a href="{url}">{title}</a>'.format(url="/shenqingvhost/%s/%s/" % (obj.pk,int(time.time())), title=u"submit")
        else:
            return u"申请已提交"
    shenqing_tijiao.short_description = u"提交申请"
    shenqing_tijiao.allow_tags = True


class guanli_vhost_zdy(admin.ModelAdmin):
    #自定义申请主键ID的字段
    def pk_zdy(self,obj):
        return obj.pk
    pk_zdy.short_description = "管理ID"

    def get_list_display(self, request):
        # 不是超级用户，显示这些字段
        if not request.user.is_superuser:
            self.list_display = ('pk_zdy','shenqing_vhost_id', 'vhost_ip')
            return self.list_display

        list_display = ('pk_zdy','shenqing_vhost_id', 'vhost_ip','shenqing_status')
        return list_display


    #不是超级用户，封锁为只读
    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            readonly_fields = ['pk_zdy','shenqing_vhost_id', 'vhost_ip']
            return readonly_fields
        return super(guanli_vhost_zdy,self).get_readonly_fields(request,obj=None)

    # 自定一个字段的方法必须写在外围
    def shenqing_status(self, obj):
        if obj.shenqing_vhost_id.shenqing_status == "2":
            return u"审核通过，可以使用了"
        else:
            return '<a href="{url}">{title}</a>'.format(
                url="/vhostshenhe2/%s/%s/" % (obj.shenqing_vhost_id.pk, int(time.time())), title=u"shenhe")

    shenqing_status.short_description = u"修改申请状态"
    shenqing_status.allow_tags = True

    #只能看到自己的容器
    def get_queryset(self, request):
        qs = super(guanli_vhost_zdy, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        get_userid = shenqing_vhost.objects.filter(user_id=request.user.id)
        get_userid = guanli_vhost.objects.filter(shenqing_vhost_id__in=get_userid)
        return get_userid


admin.site.register(idc)
admin.site.register(shenqing_vhost,shenqing_vhost_zdy)
admin.site.register(guanli_vhost,guanli_vhost_zdy)
admin.site.register(ipaddress_vhost)
