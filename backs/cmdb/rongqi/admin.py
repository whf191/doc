#coding=utf-8
from __future__ import unicode_literals
from django.contrib import admin
from models import *
import time
from django.forms import  ModelForm
from suit.widgets import  SuitDateWidget, SuitTimeWidget, SuitSplitDateTimeWidget
#全局授权用户
sudo_users = ['hejin']
qianduan_users = ["mazengliang","yangqian", "sheqiulin","wanghuan"
    ,"luochao","jiangmulan" ,"jinzeze","nielinying","liuxia","leihao","wanhaifeng"]



class shenqing_rongqi_form(ModelForm):
    class Meta:
        widgets = {
            'end_date':SuitDateWidget
          }



class shenqing_rongqi_zdy(admin.ModelAdmin):
    form = shenqing_rongqi_form
    save_on_top = True
    list_display = ('pk_zdy','shenqing_mingzi','type_rongqi_id','shenqing_status','end_date','shenqing_tijiao')
    fields = ('shenqing_mingzi','type_rongqi_id','end_date','user_id')


    #普通用户只能看到自己的申请列表
    def get_queryset(self, request):
        qs = super(shenqing_rongqi_zdy, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        get_userid = shenqing_rongqi.objects.filter(user_id=request.user.id)
        return get_userid
    #重写外键方法
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if not request.user.is_superuser:
            if db_field.name == "user_id":
                kwargs['queryset'] = User.objects.filter(pk=request.user.id)
        return super(shenqing_rongqi_zdy,self).formfield_for_foreignkey(db_field, request, **kwargs)

    #不是超级用户，封锁某些字段为只读
    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            readonly_fields = ['shenqing_status']
            return readonly_fields
        return super(shenqing_rongqi_zdy,self).get_readonly_fields(request,obj=None)
    #自定义申请提交字段的方法
    def shenqing_tijiao(self,obj):
        if  obj.shenqing_status == "4":
            return  u"""

                            <!DOCTYPE html><html>
                            <head>
                                <meta charset="UTF-8">

                                <script>
                                // 定义个a2的ajax的函数
                                    function a2(){


                                    $.ajax({
                                        url:"%s",
                                        type:"GET",

                                        success:function(req){
                                             $.messager.progress("close");
                                           // alert(req);
                                           window.location.reload();
                                        },

                                        error:function(){


                                            $.messager.progress("close");
                                            alert("不能访问服务器，请联系管理员");
                                        }


                                    });


                                };

                                    $(document).ready(function(){
                                          $("#bb").click(function(){

                                            $.messager.progress({text:"申请提交中"});
                                            a2();



                                          });
                                        });

                                </script>


                            </head>
                            <button id="bb" type="button"  class="btn btn-warning btn-xs">点我申请</button>
                            <link rel="stylesheet" type="text/css" href="/static/jquery-easyui-1.5/themes/metro/easyui.css">
    <link rel="stylesheet" type="text/css" href="/static/jquery-easyui-1.5/themes/mobile.css">
	<link rel="stylesheet" type="text/css" href="/static/jquery-easyui-1.5/themes/icon.css">
	<script type="text/javascript" src="/static/jquery-easyui-1.5/jquery.min.js"></script>
                                    <script type="text/javascript" src="/static/jquery-easyui-1.5/jquery.easyui.min.js"></script>
                                    <script type="text/javascript" src="/static/jquery-easyui-1.5/jquery.easyui.mobile.js"></script>
                            </html> """  % ("/shenqingrongqi/%s/%s/" % (obj.pk,int(time.time())))
            #return '<a href="{url}">{title}</a>'.format(url="/shenqingrongqi/%s/%s/" % (obj.pk,int(time.time())), title=u"submit")
        else:
            return u"申请已提交"
    shenqing_tijiao.short_description = u"提交申请"
    shenqing_tijiao.allow_tags = True
    #自定义申请主键ID的字段
    def pk_zdy(self,obj):
        return obj.pk
    pk_zdy.short_description = "容器申请ID"

    #干掉普通用的actions 操作
    def get_actions(self, request):
        actions = super(shenqing_rongqi_zdy, self).get_actions(request)
        if request.user.is_superuser:
            return  actions
        del actions['delete_selected']
        return  actions






class guanli_rongqi_zdy(admin.ModelAdmin):
    # 自定一个字段的方法必须写在外围
    def shenqing_status(self, obj):
        if obj.shenqing_rongqi_id.shenqing_status == "2":
            return u"审核通过，可以使用了"
        else:
            return '<a href="{url}">{title}</a>'.format(
                url="/shenhe2/%s/%s/" % (obj.shenqing_rongqi_id.pk, int(time.time())), title=u"shenhe")

    shenqing_status.short_description = u"修改申请状态"
    shenqing_status.allow_tags = True

    #定义一个外部目录的存放路径
    def waibu(self,obj):
        return '/mnt/data/'
    waibu.short_description = u'容器私有目录(容器删除,数据暂时也不会丢失)'

    #自定义申请主键ID的字段
    def pk_zdy(self,obj):
        return obj.pk
    pk_zdy.short_description = "容器管理ID"

    def qi(self,obj):
        from .rongqi_anniu import anniu2
        return  anniu2 % (obj.pk,obj.rongqi_ip.ip,obj.pk,obj.pk,obj.pk)

    qi.short_description = u"一键启动"
    qi.allow_tags = True

    def get_list_display(self, request):
        # 不是超级用户，显示这些字段
        if request.user.is_superuser:
            list_display = ('pk_zdy', 'shenqing_rongqi_id', 'rongqi_ip', 'rongqi_id', 'create_date', "shenqing_status",'external_directory')
            return list_display
        elif request.user.username in sudo_users:
            list_display = ('pk_zdy', 'shenqing_rongqi_id', 'rongqi_ip', 'rongqi_id', 'create_date', "shenqing_status",'external_directory')
            return list_display
        elif request.user.username in qianduan_users:
            list_display = ('shenqing_rongqi_id', 'rongqi_ip', 'create_date', 'waibu','qi')
            return list_display

        else:
            self.list_display = ('shenqing_rongqi_id', 'rongqi_ip', 'create_date', 'waibu')
            return self.list_display




    #不是超级用户，封锁为只读
    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser :
            readonly_fields = ['shenqing_rongqi_id','rongqi_ip','rongqi_id','create_date','external_directory']
            return readonly_fields
        return super(guanli_rongqi_zdy,self).get_readonly_fields(request,obj=None)


    # 重写外键方法
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if  request.user.is_superuser:
            if db_field.name == "shenqing_rongqi_id":
                kwargs['queryset'] = shenqing_rongqi.objects.exclude(shenqing_status='2')
        return super(guanli_rongqi_zdy, self).formfield_for_foreignkey(db_field, request, **kwargs)
    #只能看到自己的容器
    def get_queryset(self, request):
        qs = super(guanli_rongqi_zdy, self).get_queryset(request)

        if  request.user.is_superuser:
            return qs
        elif request.user.username in sudo_users:
            return qs
        get_userid = shenqing_rongqi.objects.filter(user_id=request.user.id)
        get_userid = guanli_rongqi.objects.filter(shenqing_rongqi_id__in=get_userid)
        return get_userid

    #干掉普通用的actions 操作
    def get_actions(self, request):
        actions = super(guanli_rongqi_zdy, self).get_actions(request)
        if request.user.is_superuser:
            return  actions
        del actions['delete_selected']
        return  actions


class ipaddress_rongqi_zdy(admin.ModelAdmin):
    list_display = ("ip_name","ip","is_enable")


class create_rongqi_zdy(admin.ModelAdmin):
    list_display = ("shenqing_id",'ipaddress_rongqi_id','create_date','note',"chuangjian")
    # 自定一个字段的方法必须写在外围
    def chuangjian(self, obj):
        # if obj.shenqing_rongqi_id.shenqing_status == "2":
        #     return u"审核通过，可以使用了"
        # else:
        #     return '<a href="{url}">{title}</a>'.format(
        #         url="/shenhe2/%s/%s/" % (obj.shenqing_rongqi_id.pk, int(time.time())), title=u"shenhe")

        if obj.iscreate == False:
            return u"""

                            <!DOCTYPE html><html>
                            <head>
                                <meta charset="UTF-8">

                                <script>
                                // 定义个a1的ajax的函数
                                    function a1(){


                                    $.ajax({
                                        url:"/zdy/",
                                        type:"GET",
                                        data:{'shenqing_id':"%s",'ip':"%s",'time':%s},
                                        success:function(req){
                                             $.messager.progress("close");
                                            alert(req);
                                            window.location.reload();
                                        },

                                        error:function(){


                                            $.messager.progress("close");
                                            alert("不能访问服务器，请联系管理员");
                                        }


                                    });


                                };

                                    $(document).ready(function(){
                                          $("#bb").click(function(){

                                            $.messager.progress({text:"正在创建容器"});
                                            a1();



                                          });
                                        });

                                </script>


                            </head>
                            <button id="bb" type="button"  class="btn btn-warning">创建</button>
                            <link rel="stylesheet" type="text/css" href="/static/jquery-easyui-1.5/themes/metro/easyui.css">
    <link rel="stylesheet" type="text/css" href="/static/jquery-easyui-1.5/themes/mobile.css">
	<link rel="stylesheet" type="text/css" href="/static/jquery-easyui-1.5/themes/icon.css">
	<script type="text/javascript" src="/static/jquery-easyui-1.5/jquery.min.js"></script>
                                    <script type="text/javascript" src="/static/jquery-easyui-1.5/jquery.easyui.min.js"></script>
                                    <script type="text/javascript" src="/static/jquery-easyui-1.5/jquery.easyui.mobile.js"></script>
                            </html> """ % (obj.shenqing_id,obj.ipaddress_rongqi_id.ip,int(time.time()))

        return  u" 创建完毕"



    chuangjian.short_description = u"创建容器"
    chuangjian.allow_tags = True



    # 重写外键方法
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if  request.user.is_superuser:
            if db_field.name == "ipaddress_rongqi_id":
                kwargs['queryset'] = ipaddress_rongqi.objects.filter(is_enable=False)
        return super(create_rongqi_zdy, self).formfield_for_foreignkey(db_field, request, **kwargs)

    #干掉普通用的actions 操作
    def get_actions(self, request):
        actions = super(create_rongqi_zdy, self).get_actions(request)
        if request.user.is_superuser:
            return  actions
        del actions['delete_selected']
        return  actions

admin.site.register(type_rongqi)
admin.site.register(shenqing_rongqi,shenqing_rongqi_zdy)
admin.site.register(guanli_rongqi,guanli_rongqi_zdy)
admin.site.register(ipaddress_rongqi,ipaddress_rongqi_zdy)
admin.site.register(pipaddress_rongqi)
admin.site.register(create_rongqi,create_rongqi_zdy)



