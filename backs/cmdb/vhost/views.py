#coding=utf-8
from django.shortcuts import HttpResponse,render_to_response,HttpResponsePermanentRedirect
from models import *
from django.core.mail import send_mail
import time,json,os


# Create your views here.
#容器申请...
def shenqingvhost(request,pk,c):
    if not request.user:
        return HttpResponsePermanentRedirect("/admin/vhost/shenqing_vhost/")
    pk_id = int(pk)
    rs = shenqing_vhost.objects.get(pk=pk_id)
    rs.shenqing_status =1
    rs.save()
    send_mail(u"%s虚拟主机申请通知" % rs.user_id.first_name, u"申请ID号:%s 申请用户:%s 申请用户ID:%s \n 你申请的虚拟主机，运维部已收到，请等待邮件答复" % (pk_id,rs.user_id.first_name,rs.user_id.id), 'wanhaifeng@meilele.com', ['wanhaifeng@meilele.com',rs.user_id.email],
              fail_silently=False)
    return HttpResponsePermanentRedirect('/admin/vhost/shenqing_vhost/')


#容器管理，审核
def vhostshenhe2(request,pk,c):
    if not request.user.is_superuser:
        return HttpResponsePermanentRedirect("/admin/vhost/guanli_vhost/")
    pk_id = int(pk)
    rs = shenqing_vhost.objects.get(pk=pk_id)
    rs.shenqing_status =2
    rs.save()
    #找到管理容器，再找到容器ID对应的IP
    gr = guanli_vhost.objects.get(shenqing_vhost_id=rs.pk)
    gr_ip = gr.vhost_ip.ip
    send_mail(u"%s虚拟主机审核通知" % rs.user_id.first_name, u"审核通过，你的虚拟主机IP是:%s默认用户root,密码123456" % gr_ip, 'wanhaifeng@meilele.com', [rs.user_id.email], fail_silently=False)
    return HttpResponsePermanentRedirect('/admin/vhost/guanli_vhost/')
