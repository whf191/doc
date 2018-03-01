#coding=utf-8
from __future__ import unicode_literals
from django.contrib import admin
from .models import *
from .html import moban


# Register your models here.

class  zdy_chengjibiao(admin.ModelAdmin):
    list_display = ['xuesheng_id','type_chengji_id','yuwen','shuxue','yingyu','zhengzhi','lishi','dili'

        ,'shengwu','nianji_mingci','banji_mingci']
    #filter_horizontal = ()
    raw_id_fields = ("xuesheng_id",'type_chengji_id')
    search_fields = ("xuesheng_id__name",)
    list_filter = ('type_chengji_id',)

    fieldsets = (
        ('学生和成绩类型', {'fields': (('xuesheng_id', 'type_chengji_id'),)}),
        ('科目', {'fields': ('yuwen', 'shuxue', 'yingyu', 'zhengzhi', 'lishi', 'dili', 'shengwu')}),
        ('分数', {'fields': ('zongfen', 'xiaozongfen')}),
        ('名次', {'fields': ('nianji_mingci', 'banji_mingci')}),

        ('备注', {'fields': ('Notes',)})        )

    #只能看到自己的学生
    def get_queryset(self, request):
        qs = super(zdy_chengjibiao, self).get_queryset(request)
        #如果是管理员查看所有学生
        if  request.user.is_superuser:
           return qs

        #根据用户反向方法，查询用户属于那些班级
        user = request.user
        banji_id =  user.banji_set.all()
        print banji_id
        i_b = []
        for i in banji_id:
            i_b.append(xuesheng.objects.filter(banji_id=i))
        zuhe_i_b = []
        for i in i_b:
            zuhe_i_b+=i
        print zuhe_i_b
        qs_xuesheng = chengjibiao.objects.filter(xuesheng_id__in=zuhe_i_b)
        return qs_xuesheng

    # #重写外键方法
    # def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
    #     if  request.user.is_superuser:
    #         if db_field.name == "type_chengji_id":
    #             print "+++++++++++++++++++++"
    #             user = request.user
    #             banji_id = user.banji_set.all()
    #             #kwargs['queryset'] = chengjibiao.objects.filter(banji_id__in=banji_id)
    #     return super(zdy_chengjibiao, self).formfield_for_foreignkey(db_field, request, **kwargs)



class zdy_xuesheng(admin.ModelAdmin):
    filter_horizontal = ("jiazhang_id",)
    list_display = ['pk','name','xingbie','kaohao_id','xuehao','banji_id','bind_jiazhang']
    raw_id_fields = ("kaohao_id","banji_id")
    search_fields = ("name","kaohao_id__name","jiazhang_id__name")

    def bind_jiazhang(self,obj):
        pk_jiazhang = obj
        pk_jiazhang =  pk_jiazhang.jiazhang_id.select_related()

        pk_jzs = []
        for i in pk_jiazhang:
            pk_jzs.append(i.name)

        return ",".join(pk_jzs)

    bind_jiazhang.short_description = "绑定家长"
    bind_jiazhang.allow_tags = True



    #只能看到自己的学生
    def get_queryset(self, request):
        qs = super(zdy_xuesheng, self).get_queryset(request)
        #如果是管理员查看所有学生
        if  request.user.is_superuser:
           return qs

        #根据用户反向方法，查询用户属于那些班级
        user = request.user
        banji_id =  user.banji_set.all()
        #通过in方法查询出，用户拥有那些学生

        qs_xuesheng = xuesheng.objects.filter(banji_id__in=banji_id)

        return qs_xuesheng

    #重写外键方法
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if  request.user.is_superuser:
            if db_field.name == "banji_id":
                user = request.user
                banji_id = user.banji_set.all()
                kwargs['queryset'] = banji.objects.filter(id__in=banji_id)
        return super(zdy_xuesheng, self).formfield_for_foreignkey(db_field, request, **kwargs)






class zdy_banji(admin.ModelAdmin):
    filter_horizontal = ("laoshi",)
    list_display = ['pk','name',"bind_laoshi"]
    def bind_laoshi(self,obj):
        pk = obj.pk
        pk_banji = banji.objects.get(pk=pk)
        pk_laoshi =  pk_banji.laoshi.select_related()
        print pk_laoshi
        #pk_laoshi = pk_banji.auth_user_set.all()

        pk_jzs = []
        for i in pk_laoshi:
            pk_jzs.append(i.first_name)

        return ",".join(pk_jzs)

    bind_laoshi.short_description = "绑定老师"
    bind_laoshi.allow_tags = True



class zdy_type_chengji(admin.ModelAdmin):
    list_display = ['pk','name']

class zdy_piliang_daoru(admin.ModelAdmin):
    list_display = ["pk","name","chengji_leixing","excl_file","note","create_date","daoru"]
    fields = ("name","chengji_leixing","excl_file","note")

    def daoru(self,obj):
        if obj.daoru_biaoshi == "0":
            return moban % (obj.pk,"piliang_daoru",obj.pk,obj.pk,obj.pk,obj.pk,"点击导入")
        if obj.daoru_biaoshi == "1":
            return "已经导入"

    daoru.short_description = "导入操作"
    daoru.allow_tags = True
class zdy_piliang_xuesheng_jiazhang_daoru(admin.ModelAdmin):
    list_display = ["pk","name","banji_leixing","excl_file","note","create_date","daoru"]
    fields = ("name","banji_leixing","excl_file","note")
    def daoru(self,obj):
        if obj.daoru_biaoshi == "0":
            return moban % (obj.pk,"piliang_daoru_jiazhang_xuesheng",obj.pk,obj.pk,obj.pk,obj.pk,"点击导入")
        if obj.daoru_biaoshi == "1":
            return "已经导入"

    daoru.short_description = "导入操作"
    daoru.allow_tags = True

class zdy_jiazhang(admin.ModelAdmin):
    list_display = ['pk',"name","alias","tel","weixin_id","Notes"]
    search_fields = ("name",)

class zdy_kaohao(admin.ModelAdmin):
    list_display= ['pk','name','get_xuesheng']
    search_fields = ("name",)
    def get_xuesheng(self,obj):
        pk_getxuesheng = xuesheng.objects.filter(kaohao_id=obj.pk)
        pk_jzs = []
        for i in pk_getxuesheng:
            pk_jzs.append(i.name)

        return ",".join(pk_jzs)

    get_xuesheng.short_description = "绑定学生"
    get_xuesheng.allow_tags = True





admin.site.register(jiazhang,zdy_jiazhang)
admin.site.register(kaohao,zdy_kaohao)
admin.site.register(banji,zdy_banji)
admin.site.register(xuesheng,zdy_xuesheng)
admin.site.register(type_chengji,zdy_type_chengji)
admin.site.register(chengjibiao,zdy_chengjibiao)
admin.site.register(piliang_daoru,zdy_piliang_daoru)

admin.site.register(piliang_xuesheng_jiazhang_daoru,zdy_piliang_xuesheng_jiazhang_daoru)

