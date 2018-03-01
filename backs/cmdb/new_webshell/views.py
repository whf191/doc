#coding=utf-8
from __future__ import unicode_literals
from django.shortcuts import HttpResponse,HttpResponseRedirect,render_to_response
from .models import *
from django.contrib.auth.views import login,logout
# Create your views here.


def logon(request):
    logout(request)
    ret = login(request)

    return HttpResponse(ret)

    print ret
    print repr(ret)



#daohangtiao = {"功能":[['主机操作','/get_zhuji/'],['webshell','/webshell/']]}

def get_daohangtiao():
    zjly = host_type.objects.all()
    zjly = [(i.jifang_id.name,i.name,i.url) for i in zjly]
    daohangtiao = {}
    for i in zjly:
        jifang_zhuji = i[0]
        zhuji_leixing = i[1]
        url = i[2]
        if daohangtiao.get(jifang_zhuji,None):
            daohangtiao[jifang_zhuji].append((zhuji_leixing,url))
        else:
            daohangtiao[jifang_zhuji] = []
            daohangtiao[jifang_zhuji].append((zhuji_leixing, url))

    print daohangtiao
    #daohangtiao = {"功能": []}
    #daohangtiao['功能'].append()
    return daohangtiao

daohangtiao = get_daohangtiao()


def index(request):


    return render_to_response("webshell/index.html",{'daohangtiao':daohangtiao})



def get_zhuji(request):

    host_all  = host.objects.all()
    new_all = []
    for i in host_all:
        new_all.append([i.pk,i.ip])


    return render_to_response('webshell/host.html',{'zhuji':new_all,'daohangtiao':daohangtiao})

def get_shijian(request):
    host_id = request.POST.get("pk",None)

    zhuji = host.objects.get(pk=host_id)
    shijians =  zhuji.bind_shijian.select_related()

    html_select_head = """
    
    <select id="shijian" class="form-control" ">
						<option  value="feiji">请选择</option>   
    """


						 
    html_select_tail = " </select>"
    html_select_content_start = ""

    html_select_content = "<option value=%s>%s</option>"

    if shijians:
        for i in shijians:
            html_select_content_start += html_select_content % (i.pk,i.name)
            print html_select_content_start
    html_select = html_select_head + html_select_content_start + html_select_tail



    return HttpResponse(html_select)

def get_zhixing(request):
    host_pk  = request.POST.get("host_pk",None)
    shijian_pk = request.POST.get("shijian_pk",None)

    return HttpResponse("%s,%s" % (host_pk,shijian_pk))

