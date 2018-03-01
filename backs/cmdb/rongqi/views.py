#coding=utf-8
from  __future__ import unicode_literals
from django.shortcuts import HttpResponse,render_to_response,HttpResponsePermanentRedirect
from models import *
import  models
from django.core.mail import send_mail
import docker_mll,time,json,os,requests
from yuanchenglianjie import Docker_fenpei_ip

def index(request):
    return HttpResponsePermanentRedirect('/admin')



#容器管理，审核
def shenhe2(request,pk,c):
    if not request.user.is_superuser:
        return HttpResponsePermanentRedirect("/admin/rongqi/guanli_rongqi/")
    pk_id = int(pk)
    rs = shenqing_rongqi.objects.get(pk=pk_id)
    rs.shenqing_status =2
    rs.save()
    #找到管理容器，再找到容器ID对应的IP
    gr = guanli_rongqi.objects.get(shenqing_rongqi_id=rs.pk)
    gr_shenqing_mz = gr.shenqing_rongqi_id.shenqing_mingzi
    gr_ip = gr.rongqi_ip.ip
    send_mail(u"%s容器审核通知" % rs.user_id.first_name, u"审核通过，你的%s容器IP是:%s默认用户root,密码123456" % (gr_shenqing_mz,gr_ip), 'wanhaifeng@meilele.com', [rs.user_id.email], fail_silently=False)
    return HttpResponsePermanentRedirect('/admin/rongqi/guanli_rongqi/')

#容器申请...
def shenqingrongqi(request,pk,c):
    if not request.user:
        return HttpResponsePermanentRedirect("/admin/rongqi/shenqing_rongqi/")
    pk_id = int(pk)
    rs = shenqing_rongqi.objects.get(pk=pk_id)
    rs.shenqing_status =1
    rs.save()
    send_mail(u"%s容器申请通知" % rs.user_id.first_name, u"申请ID号:%s 申请用户:%s 申请用户ID:%s \n 你申请的容器，运维部已收到，请等待邮件答复" % (pk_id,rs.user_id.first_name,rs.user_id.id), 'wanhaifeng@meilele.com', ['wanhaifeng@meilele.com',rs.user_id.email],
              fail_silently=False)
    return HttpResponsePermanentRedirect('/admin/rongqi/shenqing_rongqi/')

#以下是容器创建api接口部分

def create_rongqi(request,zidian):
    cj = request.GET.get('cj',None)
    print cj
    zidian = json.loads(cj)
    select_rongqi_ip = zidian['ip_zu'][0]
    select_pip = zidian['ip_zu'][1]
    select_pid = zidian['ip_zu'][2]
    select_shenqing_id = zidian['shenqing_id'][0]
    select_rongqi_type = zidian['shenqing_id'][1]
    external_directory = "/var/opt/%s_%s" % (select_shenqing_id,int(time.time()))
    external_directory_apps = external_directory + "/apps"
    external_directory_logs = external_directory + "/logs"
    rs_select_ppasswd = pipaddress_rongqi.objects.get(pk=select_pid)
    select_gateway = rs_select_ppasswd.geteway
    select_ppasswd = rs_select_ppasswd.password
    print zidian,"+++++++--------------------------------"

    # #根据申请ID创建外部目录
    try:
        print select_ppasswd ,"+++++++++++++++++++++++++++++"
        yc = Docker_fenpei_ip(select_pip, 'root', select_ppasswd)
        yc.run("/usr/bin/mkdir -p %s" % external_directory)
        yc.run("/usr/bin/mkdir -p %s" % external_directory_apps)
        yc.run("/usr/bin/mkdir -p %s" % external_directory_logs)

    except Exception,e:
        print u"创建外部目录失败"
        f = open("/root/p.log",'a+')
        f.write(e)
        f.close()
        return False


    # 连接容器服务器
    print "%s,++++++++++++++++++++++" % select_pip
    rongqi = docker_mll.Docker_mll(base_url="tcp://%s:2375" % select_pip)
    # 获取容器信息
    print rongqi.containers()
    # 开始创建容器信息
    rs_rongqi_id = rongqi.create_container(select_rongqi_ip,select_pip,select_rongqi_type,select_shenqing_id,external_directory)
    response = rongqi.start(rs_rongqi_id)

    #判断是否成功
    if not rs_rongqi_id:
        return False

    #把容器ID写入容器管理表
    try:

        get_shenqing_id = shenqing_rongqi.objects.get(pk=select_shenqing_id)

        get_ip = ipaddress_rongqi.objects.get(ip=select_rongqi_ip)
        gr = guanli_rongqi(shenqing_rongqi_id=get_shenqing_id,rongqi_ip=get_ip,rongqi_id=rs_rongqi_id,external_directory=external_directory)
        gr.save()

        get_ip = ipaddress_rongqi.objects.get(ip=select_rongqi_ip)
        get_ip.is_enable =True
        get_ip.save()

        #连接宿主服务器，分配静态IP

        #以后分配的主机，网关采用数据库配置试
        ycrs = yc.run(" /usr/sbin/pipework br0 %s %s/22@%s" % ( rs_rongqi_id[:12],select_rongqi_ip,select_gateway))
        crr = models.create_rongqi.objects.get(shenqing_id=int(select_shenqing_id))
        crr.iscreate = True
        crr.save()

    except Exception,e:
        print e,u"容器创建失败"
        return HttpResponse(0)
     # 创建成功，写入

    # 如果容器创建成功，修改创建容器状态


    return HttpResponse(1)


def get_rongqi_type_shenqing_id(request,pk):
    get_rongqitype = docker_mll.my_custom_sql(pk)
    print get_rongqitype
    return HttpResponse(json.dumps(get_rongqitype))

def get_ip(request):
    rs_getip = docker_mll.get_ip_sql()
    return HttpResponse(json.dumps(rs_getip))

def is_shenqing(request,pk):
    try:
        s1 = shenqing_rongqi.objects.get(pk=pk)
    except  Exception,e:
        return HttpResponse(json.dumps(3))

    try:
        gr = guanli_rongqi.objects.get(shenqing_rongqi_id=s1)
    except Exception,e:
        return HttpResponse(json.dumps(1))
    return HttpResponse(json.dumps(2))

#获取指定服务器的容器

def get_start_docker(request):
    pip = request.GET.get("pip",None)
    error = json.dumps("1")
    if not pip:
        #为空，传个1
        return  HttpResponse(error)
    rs = docker_mll.get_start_pip(pip)
    if len(rs) == 0:
        return HttpResponse(error)
    rs = json.dumps(rs)
    return  HttpResponse(rs)


#玩转admin自定义

def admin_zdy(request,message=None):
    cmdb_url = "http://192.168.0.17"
    #获取申请ID
    rs_id = request.GET.get("shenqing_id",None)
    # 获取容器绑定的IP
    rs_ip = request.GET.get("ip",None)

    #判断ID是否被创建
    rs_cis = check_is_shenqi_id(shenqing_id=rs_id,cmdb_url=cmdb_url)
    if rs_cis == 2 or rs_cis == 3:
        return HttpResponse(u"id存在或不存在，创建失败")

    rs_cd = create_docker(shenqing_id=rs_id,ip=rs_ip)

    return HttpResponse(u"创建成功")

#创建docker主函数
def  create_docker(shenqing_id,ip,cmdb_url="http://192.168.0.17"):
    zidian = {'shenqing_id': None, "ip_zu": None}
    rs_shenqing_id_type = get_shenqing_id(cmdb_url,shenqing_id)
    zidian['shenqing_id'] = rs_shenqing_id_type
    rs_get_ip = get_ips(cmdb_url,ip)
    zidian['ip_zu'] = rs_get_ip
    f6 = requests.get("%s/create_rongqi/chaungjian/?cj=%s" % (cmdb_url, json.dumps(zidian)))


#检查id是否存在
def check_is_shenqi_id(shenqing_id,cmdb_url):
    is_shenqi_id = requests.get("%s/is_shenqing/%s" % (cmdb_url, shenqing_id))
    is_shenqi_id = str(is_shenqi_id.json()).strip()
    if is_shenqi_id == "2":
        return 2
        #return HttpResponse(u"id存在，不能继续，退出")
    elif is_shenqi_id == "3":
        return 3
        #return HttpResponse(u"申请ID不存在，退出")

#获取申请ID的类型
def get_shenqing_id(cmdb_url,shenqing_id):
    rs_type = requests.get("%s/get_rongqi_type_shenqing_id/%s" % (cmdb_url, shenqing_id))
    rs_type = rs_type.json()[0]
    return rs_type

#获取IP组
def get_ips(cmdb_url,ip):
    f3 = requests.get("%s/get_ip" % cmdb_url)
    f3 = f3.json()
    for i in f3:
        if ip in i:
            return i
    return None



#表单提交过来的申请ID，和服务器组IP的回调创建容器方法
def call_create_rongqi(request):
    ipzu2 =[]
    zidian = {}
    shenqing_id =  request.GET.get("shenqing_id",None)
    ip_zu = request.GET.get("ip_zu",None)
    if not shenqing_id and not ip_zu:
        return HttpResponsePermanentRedirect('/zdy/')

    rs_isid = is_shenqingid(shenqing_id)
    if rs_isid == 3:
        return  HttpResponse(u"ID不存在")

    elif rs_isid == 1:
        return HttpResponse(u"此ID已经申请")


    ip_zu = json.dumps(ip_zu)
    ip_zu = ip_zu.split("--")
    ipzu2.append(ip_zu[0][1:] )
    ipzu2.append(ip_zu[1][:-1])
    zidian['ip_zu'] = ipzu2
    zidian['shenqing_id'] = shenqing_id
    zidian = json.dumps(zidian)

    return HttpResponsePermanentRedirect('/create_rongqi/?cj=%s' % zidian)

def is_shenqingid(pk):
    try:
        s1 = shenqing_rongqi.objects.get(pk=pk)
    except  Exception, e:
        return 3
    try:
        gr = guanli_rongqi.objects.get(shenqing_rongqi_id=s1)
    except Exception, e:
        return 1
    return 2


def qianduan_qi(request):
    import commands
    IP = request.GET.get('ip',None)

    
    r_shell = commands.getstatusoutput(""" ansible %s -m shell -a '/bin/sh /opt/shell/qi.sh ' """ % IP)
    if r_shell[0] == 0:
        return  HttpResponse("执行远程脚本成功")
    else:
        return HttpResponse("远程执行失败")









