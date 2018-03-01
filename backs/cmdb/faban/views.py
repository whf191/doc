#coding=utf-8
from __future__ import unicode_literals
from django.shortcuts import render,HttpResponse,HttpResponsePermanentRedirect,render_to_response
from django.contrib.auth.models import User
from .models import *
import multiprocessing
from django.core.mail import send_mail
from .admin import sjc
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required
def faban_shenqing(request):
    sq = request.GET.get("shenqing_id",None)
    if sq:
        f_up = faban_upload.objects.get(pk=sq)
        f_up_shenqing_id = f_up.shenqing
        f_up_note = f_up.note
        if f_up_shenqing_id == '0':
            f_up.shenqing = '1'
            f_up.shijiancuo= sjc()
            f_up.save()

            user_id =  request.GET.get("user_id",None)
            gufe = get_user_recipient_list_email(user_id)
            if isinstance(gufe,list):
                f_leixing = request.GET.get("faban_leixing",None)
                #更新为异步方法
                t = multiprocessing.Process(target=faban_email,args=("有新的%s发版任务来了" % f_leixing, "申请%s发版主键(PK)为:%s，\n\n\n  %s  \n \n 负责人快去审核吧..." %
                        (f_leixing,sq,f_up_note),gufe ))
                #阻塞方法
                # faban_email("有新的%s发版任务来了" % f_leixing,"申请%s发版主键(PK)为:%s，\n\n\n  %s  \n \n 负责人快去审核吧..." %
                #         (f_leixing,sq,f_up_note),recipient_list=gufe )
                t.start()
                t.join()
                return HttpResponse("申请成功")
            elif gufe == 1:
                return HttpResponse("收件人为空，申请失败")
            else:
                return HttpResponse("申请失败，程序异常，联系管理员")

        else:
            return HttpResponse("请不要重复申请...")

    return HttpResponse(u"申请id为空")
@login_required
def faban_queren(request):
    sq = request.GET.get("shenqing_id",None)
    if sq:
        user_id = request.GET.get("user_id", None)
        gufe = get_user_yunwei_recipient_list_email(user_id)
        if isinstance(gufe,list):
            f_up = faban_upload.objects.get(pk=sq)
            f_up_shenqing_id = f_up.shenqing
            f_up_note = f_up.note
            if f_up_shenqing_id == "1":
                f_up.shenqing = "2"
                f_up.save()
                f_leixing = request.GET.get("faban_leixing", None)
                t = multiprocessing.Process(target=faban_email,args=("%s发版审核通过..." % f_leixing,
                                                              "审核通过的%s发版主键(PK)为:%s，\n\n\n  %s \n\n 运维工作人员处理吧..." %
                                                              (f_leixing, sq, f_up_note),gufe
                                                              ))
                t.start()

                # faban_email("%s发版审核通过..." % f_leixing,"审核通过的%s发版主键(PK)为:%s，\n\n\n  %s \n\n 运维工作人员处理吧..." %
                #             (f_leixing,sq,f_up_note),recipient_list=gufe )

                return HttpResponse("确认成功")
            else:
                return HttpResponse("请不要重复确认...")
        elif gufe == 1:
            return HttpResponse("收件人为空，申请失败")
        else:
            return HttpResponse("确认失败，程序异常，联系管理员")




def faban_email(title,content,recipient_list,from_email="it@meilele.com"):
    send_mail(title,
              content,
              from_email,recipient_list,fail_silently=False)



#通过用户user_id找到想关的程序收件人列表
def get_user_recipient_list_email(id):
    try:
        userinfo = extend_user_permissions.objects.get(user_id=id)
        userinfo_email = userinfo.recipient_list_email_id.select_related().all()
        get_userinfo_email = map(lambda x:x.user_id.email,userinfo_email)
        if len(get_userinfo_email) == 0:
            return 1

        return get_userinfo_email
    except:
        return False

def get_user_yunwei_recipient_list_email(id):
    try:
        userinfo = extend_user_permissions.objects.get(user_id=id)
        userinfo_email = userinfo.yunwei_recipient_list_email_id.select_related().all()
        get_userinfo_email = map(lambda x:x.user_id.email,userinfo_email)
        if len(get_userinfo_email) == 0:
            return 1

        return get_userinfo_email
    except:
        return False


#发版审核按钮...

def faban_shenhe(request):
    if not request.session.get('userid',None):
        return  HttpResponse("faban_shenhe...out...")
    pk = request.POST.get("pk",None)
    if not pk:
        return HttpResponse("ID不存在,审核失败")
    try:
        r_w = faban_upload.objects.get(pk=pk)
        #更改审核按钮为2
        r_w.shenhe = "2"
        r_w_userid = r_w.faban_user.id
        f_leixing = r_w.faban_types_id.name
        f_shenqing = r_w.shenqing
        r_w.save()

    except:
        return HttpResponse("db里没有pk此主键")

    gufe = get_user_yunwei_recipient_list_email(r_w_userid)
    if f_shenqing == "5":
        faban_email("编号为:%s ,%s版本已回滚..." % (f_leixing, pk), "版本已回滚", recipient_list=gufe)
    faban_email("编号为:%s ,%s版本已发..." % (f_leixing,pk), "版本已发" , recipient_list=gufe)
    return HttpResponse("审核通过")





