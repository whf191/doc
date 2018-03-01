#coding=utf-8
from __future__ import unicode_literals
from django.contrib import admin
from .models import *
from .html import moban
from django.contrib import messages
from .views import get_user_yunwei_recipient_list_email,faban_email

class zdy_faban_upload(admin.ModelAdmin):
    fields  =('faban_types_id','upfile','note','faban_user')

    # #重写save保存方法
    # def save_form(self, request, form, change):
    #     import tempfile,zipfile
    #     f_index,f_file = tempfile.mkstemp()
    #     get_zip =  request.FILES['upfile']
    #     print get_zip,dir(get_zip),type(get_zip)
    #
    #     f = open(f_file,'wb')
    #     f.write(get_zip.read())
    #     f.close()
    #
    #     f_zipfile= zipfile.ZipFile(f_file,'r')
    #     print f_zipfile.filelist[0].filename
    #
    #     return super(zdy_faban_upload,self).save_form(request,form,change)

    #发版审核用户封锁为只读
    def get_readonly_fields(self, request, obj=None):
        user_id = request.user.id
        user_id_ex = extend_user_permissions.objects.get(user_id=user_id).permissions
        if user_id_ex == "2":
            readonly_fields = ['faban_types_id','upfile','faban_user','note']
            return readonly_fields
        return super(zdy_faban_upload,self).get_readonly_fields(request,obj=None)



    #定制回滚按钮...
    actions = ['make_huigun']
    def make_huigun(self,request,queryset):
        xuanze = queryset.all()
        if len(xuanze) == 1 :
            xuanze_one = xuanze[0]
            if xuanze_one.shenqing  == '3':
                xuanze_one.shenqing = "4"
                xuanze_one.shenhe = "0"
                xuanze_one.save()
                gufe = get_user_yunwei_recipient_list_email(request.user.pk)
                f_leixing= xuanze_one.faban_types_id.name
                sq = xuanze_one.pk
                faban_email("%s回滚申请提交..." % f_leixing, "%s回滚主键(PK)为:%s，运维工作人员处理吧..." %
                            (f_leixing, sq), recipient_list=gufe)
                messages.success(request, "回滚已经提交,等待运维工作人员处理")
        else:
            messages.warning(request,"不能多选，只能选择一个")
    make_huigun.short_description = "回滚，多选不生效"



    def shenqing_anniu(self,obj):
        if obj.shenqing == "0":

            return moban % (obj.pk,'faban_shenqing',obj.pk,obj.faban_user.pk,obj.faban_user.email,obj.faban_types_id.name,obj.pk,obj.pk,obj.pk,'申请')
        elif obj.shenqing == "1":
            return "申请已成功提交"
        elif obj.shenqing == "2":
            return "负责人已确认，等待运维处理"
        elif obj.shenqing == "3":
            return "版本已发"
        elif obj.shenqing == "4":
            return "回滚申请已提交，等待运维处理"
        elif obj.shenqing == "5":
            return "版本已回滚"


    shenqing_anniu.short_description = "申请"
    shenqing_anniu.allow_tags = True
    def queren_anniu(self,obj):
        if obj.shenqing == "0":
            return "还未申请"
        elif obj.shenqing == "1":
            return moban % (obj.pk,'faban_queren',obj.pk,obj.faban_user.pk,obj.faban_user.email,obj.faban_types_id.name,obj.pk,obj.pk,obj.pk,'确认')
        elif obj.shenqing == "2":
            return "已确认"
        elif obj.shenqing == "3":
            return "版本已发"
        elif obj.shenqing == "4":
            return "回滚申请已提交，等待运维处理"
        elif obj.shenqing == "5":
            return "版本已回滚"

    queren_anniu.short_description = "确认"
    queren_anniu.allow_tags = True


    def get_list_display(self, request):
        # 根据不同的用户显示不同的字段
        one_user = extend_user_permissions.objects.get(user_id=request.user)

        if one_user.permissions == "1":
            self.list_display = ('pk','faban_types_id','upfile','shenqing_anniu')
            return self.list_display
        else:
            list_display = ('pk','faban_types_id','upfile','queren_anniu')
        return list_display


    #重写外键方法 --根据用户的类型，返回不同的发版权限
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if not request.user.is_superuser or request.user.is_superuser :
            if db_field.name == "faban_types_id":
                    try:
                        ss = extend_user_permissions.objects.get(user_id=request.user)
                        kwargs['queryset'] = ss.faban_types_many_id.select_related().all()
                    except:
                        kwargs['queryset'] = faban_types.objects.filter(wu_id="1")

            elif db_field.name == 'faban_user':
                kwargs['queryset'] = User.objects.filter(pk=request.user.id)

        return super(zdy_faban_upload,self).formfield_for_foreignkey(db_field, request, **kwargs)



    #干掉普通用户的删除操作
    def get_actions(self, request):
        actions = super(zdy_faban_upload, self).get_actions(request)
        if request.user.is_superuser:
            return  actions
        del actions['delete_selected']
        return  actions







class zdy_jgz_faban_php(admin.ModelAdmin):
    list_display = ["faban_leixing","url_zip","url_zip_md5","faban_id","state","create_date"]



admin.site.register(faban_types)
admin.site.register(extend_user_permissions)
admin.site.register(faban_upload,zdy_faban_upload)
admin.site.register(recipient_list_email)
admin.site.register(yunwei_recipient_list_email)
admin.site.register(fu_faban_type)
admin.site.register(jgz_faban_php,zdy_jgz_faban_php)
admin.site.register(jgz_huigun_php)
admin.site.register(jgz_renwu)