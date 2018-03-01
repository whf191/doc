#coding=utf-8
from __future__ import unicode_literals
from django.contrib import admin
from django.forms import ModelForm
from .models import  *
from suit_redactor.widgets import RedactorWidget
from suit_ckeditor.widgets import CKEditorWidget
from suit.widgets import  SuitDateWidget, SuitTimeWidget, SuitSplitDateTimeWidget
import time


class PageForm2(ModelForm):
    class Meta:
        widgets = {
           # 'node':CKEditorWidget(editor_options={'startupFocus':True})
            #'beizhu': RedactorWidget(editor_options={'lang': 'en'}),
            'create_end': SuitDateWidget
        }

class zdy_shijian(admin.ModelAdmin):
    form = PageForm2

    search_fields = ['beizhu','fujian']
    list_filter = ('leixing_id',)
    fields = ('leixing_id', 'fujian', 'create_end', 'user_id','beizhu')
    #普通用户只能看到自己的申请列表
    def get_queryset(self, request):
        qs = super(zdy_shijian, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        get_userid = shijian.objects.filter(user_id=request.user.id)
        return get_userid

    def shenqingzhuangtai(self,obj):
        if obj.is_shenqing == '0':
            return  u"""

                            <!DOCTYPE html><html>
                            <head>
                                <meta charset="UTF-8">

                                <script>
                                // 定义个a2的ajax的函数
                                    function a2bb(){


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
                                            a2bb();



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
                            </html> """  % ("/gongdan_shenqing/%s/%s/" % (obj.pk,int(time.time())))
        elif obj.is_shenqing=='1':
            return u"申请已提交"
        elif obj.is_shenqing=="2":
            return u"已处理"
    shenqingzhuangtai.short_description="申请"
    shenqingzhuangtai.allow_tags = True

    def chulizhuangtai(self,obj):
        print obj.is_chuli,obj.is_shenqing

        if  (obj.is_shenqing=="1" or obj.is_shenqing=="0"):
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
                                          $("#bbchuli").click(function(){

                                            $.messager.progress({text:"申请提交中"});
                                            a2();



                                          });
                                        });

                                </script>


                            </head>
                            <button id="bbchuli" type="button"  class="btn btn-warning btn-xs">点我处理</button>
                            <link rel="stylesheet" type="text/css" href="/static/jquery-easyui-1.5/themes/metro/easyui.css">
    <link rel="stylesheet" type="text/css" href="/static/jquery-easyui-1.5/themes/mobile.css">
	<link rel="stylesheet" type="text/css" href="/static/jquery-easyui-1.5/themes/icon.css">
	<script type="text/javascript" src="/static/jquery-easyui-1.5/jquery.min.js"></script>
                                    <script type="text/javascript" src="/static/jquery-easyui-1.5/jquery.easyui.min.js"></script>
                                    <script type="text/javascript" src="/static/jquery-easyui-1.5/jquery.easyui.mobile.js"></script>
                            </html> """  % ("/gongdan_chuli/%s/%s/" % (obj.pk,int(time.time())))
        else:
            return "已处理"

    chulizhuangtai.short_description = "处理"
    chulizhuangtai.allow_tags = True

    # 不是超级用户，显示这些字段
    def get_list_display(self, request):
        if not request.user.is_superuser:
            self.list_display = ('pk','leixing_id', 'fujian', 'shenqingzhuangtai')
            return self.list_display

        list_display = ('pk','user_id','leixing_id', 'fujian', 'shenqingzhuangtai', 'chulizhuangtai')
        return list_display

    #重写外键方法
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if not request.user.is_superuser:
            if db_field.name == "user_id":
                kwargs['queryset'] = User.objects.filter(pk=request.user.id)
        return super(zdy_shijian,self).formfield_for_foreignkey(db_field, request, **kwargs)

    #不是超级用户，封锁某些字段为只读
    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            try:
                if obj.is_shenqing == "1" or obj.is_shenqing=="2":
                    readonly_fields = ['leixing_id','fujian','create_end', 'user_id', 'beizhu']
                    return readonly_fields
            except:
                pass
        return super(zdy_shijian,self).get_readonly_fields(request,obj=None)

admin.site.register(leixing)
admin.site.register(shijian,zdy_shijian)