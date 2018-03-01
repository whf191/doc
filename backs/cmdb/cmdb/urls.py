#coding=utf-8
"""cmdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^$','rongqi.views.index'),
    url(r'^admin/', admin.site.urls),

    #模拟登录
    # url(r'^ml','cmdb.views.ml'),

url(r'^shenhe2/(\d+)/(\d+)/$','rongqi.views.shenhe2'),
url(r'^shenqingrongqi/(\d+)/(\d+)/$','rongqi.views.shenqingrongqi'),

url(r'^create_rongqi/(\w+)/$','rongqi.views.create_rongqi'),

url(r'^get_rongqi_type_shenqing_id/(\d+)/$','rongqi.views.get_rongqi_type_shenqing_id'),
url(r'^get_ip/$','rongqi.views.get_ip'),
url(r'^is_shenqing/(\d+)/$','rongqi.views.is_shenqing'),
url(r'^get_start_docker/$','rongqi.views.get_start_docker'),
url(r'^zdy/$','rongqi.views.admin_zdy'),
url(r'^call_create_rongqi/$','rongqi.views.call_create_rongqi'),
url(r'^qianduan_qi/$','rongqi.views.qianduan_qi'),


#虚拟主机部分
url(r'^shenqingvhost/(\d+)/(\d+)/$','vhost.views.shenqingvhost'),

url(r'^vhostshenhe2/(\d+)/(\d+)/$','vhost.views.vhostshenhe2'),



#审计部分
url(r'^get_hosts/$','baoleiji.views.get_hosts'),
url(r'^post_log/$','baoleiji.views.post_log'),

#监狱系统

url(r'^get_gongong_shell/$','baoleiji.views.get_gongong_shell'),
url(r'^get_zhuji_mulu_wenjian/$','baoleiji.views.get_zhuji_mulu_wenjian'),


#微信部分
url(r'^weixin/$','weixin.views.home'),
url(r'^yw/$','weixin.views.weixin'),
url(r'^java8686/$','weixin.views.java8686'),
url(r'^shell/$','weixin.views.shell'),
url(r'^renwu/$','weixin.views.renwu'),
url(r'^send_weixin/$','weixin.views.send_weixin'),
url(r'^renwuxiangqing/$','weixin.views.renwuxiangqing'),


#更新密码
url(r'^gengxin_mima','idc.views.gengxin_mima'),



#工单部分
url(r'^gongdan_shenqing/(\d+)/(\d+)','gongdan.views.gongdan_shenqing'),

#发版部分
# url(r'^faban_shenqing/$','faban.views.faban_shenqing'),
# url(r'^faban_queren/$','faban.views.faban_queren'),
# url(r'^php_faban/$','weixin.views.php_faban'),
# url(r'^faban_shenhe/$','faban.views.faban_shenhe'),
url(r'^faban_php_new/$','faban.jgz_views.faban_php_new'),
url(r'^api_faban_php/$','faban.jgz_views.api_faban_php'),
url(r'^xin_php_faban/$','faban.jgz_views.xin_php_faban'),
url(r'^huigun_php_new/$','faban.jgz_views.huigun_php_new'),
url(r'^xin_renwu/$','faban.jgz_views.xin_renwu'),
url(r'^xin_renwuxiangqing/$','faban.jgz_views.xin_renwuxiangqing'),
url(r'^xin_php_huigun/$','faban.jgz_views.xin_php_huigun'),
url(r'^faban_login/$','faban.jgz_views.faban_login'),
url(r'^faban_login_out/$','faban.jgz_views.faban_login_out'),


# baishi....
url(r'^baishi/$','baishi.views.baishi'),

url(r'^chengji/$','baishi.views.chengji'),
url(r'^cj_chaxun/$','baishi.views.cj_chaxun'),
url(r'^piliang_daoru/$','baishi.views.daoru'),
url(r'^piliang_daoru_jiazhang_xuesheng/$','baishi.views.daoru2'),
url(r'^cj_zoushi_chaxun/$','baishi.views.cj_zoushi_chaxun'),
url(r'^cj_zhoushi/$','baishi.views.cj_zhoushi'),
url(r'^xiazai/$','baishi.views.xiazai'),
url(r'^chengji2/$','baishi.views.chengji2'),
url(r'^cj_chaxun2/$','baishi.views.cj_chaxun2'),


#logcaiji 日志采集部分

url(r'^postlog/$','logcaiji.views.postlog'),


#new_webshell...
url(r'^new_webshell_index/$','new_webshell.views.index'),
url(r'^get_zhuji/$','new_webshell.views.get_zhuji'),
url(r'^get_shijian/$','new_webshell.views.get_shijian'),
url(r'^get_zhixing/$','new_webshell.views.get_zhixing'),
url(r'^logon/$','new_webshell.views.logon'),


#dockermanageplatfrom


url(r'^is_container_config/$','dockermanageplatform.views.is_container_config'),

url(r'^get_contalner_script/$','dockermanageplatform.views.get_contalner_script'),

url(r'^is_container_create/$','dockermanageplatform.views.is_container_create'),
url(r'^remote_call_script/$','dockermanageplatform.views.remote_call_script'),



#online_logs_download
url(r'^list_online_logs/$','online_logs_download.views.list_online_logs'),
url(r'^get_online_log/$','online_logs_download.views.get_online_log'),


]









