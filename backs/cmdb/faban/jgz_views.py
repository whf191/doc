#coding=utf-8
from  __future__ import  unicode_literals
from django.contrib.auth import authenticate
from django.shortcuts import  HttpResponse,HttpResponseRedirect,render_to_response
from .models import jgz_faban_php,jgz_huigun_php,jgz_renwu
from django.db import connection
import json,uuid,subprocess,multiprocessing

"""
接入架构组的PHP发版

{'type':'php','url_zip':'http://xxx/xxx.zip','url_zip_md5':'xxxxxxxxxxxx','id':'xxxxxxxxxxx','state':[1,2]}
1正常 2回滚
流程：
1.架构组的发版平台传个参数给我，我收到一封邮件提示并记录到数据库
2.我点发版按钮，（下载zip包，比对md5是否一致，一致就生成发版任务不一致，提示错误，重新点击发版）
3.调用脚本发版，生成发版日志
4.检测发版日志,或邮件提示

"""

"""
pc版的登录页面
"""


def faban_login(request):
    #del request.session['userid']


    if request.session.get('userid', False):
        return HttpResponseRedirect('/faban_php_new/')


    username = request.POST.get("username", None)
    password = request.POST.get("password", None)
    if username and password:
        renzhen = authenticate(username=username,password=password)
        if  renzhen  is  not None:
                request.session['userid'] = username
                return HttpResponse("success")
        else:
            return HttpResponse("fail")
    return render_to_response("jgz/login.html")


def faban_login_out(request):
    if request.session.get("userid",None):
        del request.session["userid"]
        return HttpResponseRedirect('/faban_login/')
    return HttpResponse(None)



#发版上传接口

def api_faban_php(request):
    if request.method == "POST":
        php_json = request.POST.get('php_json',None)
        try:
            php_json = json.loads(php_json,encoding="utf8")
        except Exception,e:
            return HttpResponse("""{"state":"fail","message":"json解析失败:%s"}""" % e )

        faban_leixing = php_json.get('type',None)
        url_zip  = php_json.get('url_zip',None)
        url_zip_md5 = php_json.get('url_zip_md5',None)
        faban_id  = php_json.get('id',None)
        state  = php_json.get('state',None)
        if state is not None:
            state = str(state).strip()

        if url_zip is not None:
            url_zip = str(url_zip).strip()

        if url_zip_md5 is not None:
            url_zip_md5 = str(url_zip_md5).strip()

        if faban_id is not None:
            faban_id = str(faban_id).strip()

        if faban_leixing is not None:
            faban_leixing = str(faban_leixing).strip()

        if not (faban_leixing and url_zip and url_zip_md5 and faban_id and state):
            return HttpResponse(""" {"state":"fail","message":"传过来的参数不完整
            faban_leixing:%s,url_zip:%s,url_zip_md5:%s,faban_id:%s,state:%s"} """ %
                                (faban_leixing,url_zip,url_zip_md5,faban_id,state) )

        #状态为1，表示发版，2为回滚
        if state == "1":
            # 数据库查询，检查这个时间戳是不是存在，存在返回提示

            shijiancuo = jgz_faban_php.objects.filter(faban_id=faban_id)

            if len(shijiancuo) >0:
                return HttpResponse("""{"state":"fail","message":"不要重复提交，时间戳:%s,已经存在，
                    发版状态为:%s(注:1为正常录入发版数据库，3为已经发版)" } """ % (faban_id, state))
            else:
                shijiancuo = jgz_faban_php.objects.create(faban_leixing=faban_leixing, url_zip=url_zip,
                                                          url_zip_md5=url_zip_md5
                                                          , faban_id=faban_id, state=state)
                return HttpResponse(""" {"state":"success","message":"提交成功,等待运维处理"} """)

        elif state == "2":

            huigun_shijianchuo = jgz_huigun_php.objects.filter(faban_id=faban_id)

            print len(huigun_shijianchuo)
            if len(huigun_shijianchuo) >0:
                return HttpResponse("""{"state":"fail","message":"回滚记录已存在，不能重复提交"}""")

            else:
                huigun_shijianchuo = jgz_huigun_php.objects.create(faban_id=faban_id, state=state)
                huigun_shijianchuo.save()
                return HttpResponse("""{"state":"sucess","message":"回滚记录提交成功，等待运维处理"}""")
        else:
            return HttpResponse("""{"state":"fail","message":"state参数不符"}""")
    return HttpResponse(None)


def faban_php_new(request):
    if not request.session.get('userid', False):
        return HttpResponse("离开吧")
    jfp = jgz_faban_php.objects.filter(state="1")

    jfp_list = []
    if len(jfp) > 0:
        for i in jfp:
            jfp_list.append([i.pk,i.faban_leixing,i.url_zip,i.url_zip_md5,i.faban_id,i.state])
    else:
        jfp_list = False
    print jfp_list
    return render_to_response("jgz/phpfaban.html", {'daohangtiao': daohang(),'jfp_list':jfp_list})

def huigun_php_new(request):
    if not request.session.get('userid', False):
        return HttpResponse("离开吧")
    jhp = jgz_huigun_php.objects.filter(state="2")
    jhp_list = []
    if len(jhp) > 0:
        for i in jhp:
            jhp_list.append([i.pk,i.faban_id,i.state])
    else:
        jfp_list = False
    return render_to_response("jgz/phphuigun.html", {'daohangtiao': daohang(),'jhp_list':jhp_list})


def sup_shell(jiaoben,shijiancuo,userid,one_id,fa_hui,url_zip,url_zip_md5):
    subprocess.call(
        "nohup %s %s %s %s  %s %s %s &" % (
        jiaoben, shijiancuo, userid, one_id, fa_hui, url_zip, url_zip_md5),
        shell=True)
    return True

def xin_php_faban(request):
    if not request.session.get('userid', False):
        return HttpResponse("离开吧")
    if request.method == "POST":
        pk = request.POST.get("pk",None)
        if pk:
            try:
                jfp = jgz_faban_php.objects.get(pk=pk)
                if jfp.state == "1":
                    jiaoben = '/root/shell/php_faban_jgz.sh'
                    ##request.session['userid']
                    fa_hui = "1"
                    one_id = one_uuid()
                    t = multiprocessing.Process(target=sup_shell, args=(jiaoben,jfp.faban_id, request.session.get('userid', False),
                                                                        one_id, fa_hui, jfp.url_zip, jfp.url_zip_md5
                                                                          ))
                    t.start()

                    jgz_renwu.objects.create(faban_id=jfp.faban_id,state=jfp.state,jilu_log=one_id)
                    jfp.state = 3
                    jfp.save()
                    return HttpResponse("任务已经生成uuid:%s" % one_id)
                elif jfp.state == "3":
                    return HttpResponse("任务已经进入后台处理，详情查看任务记录")
                else:
                    return HttpResponse("state参数不符，出大事，运维检测")
            except Exception,e:
                return HttpResponse("pk(%s)不存:%s" % (pk,e))


def xin_php_huigun(request):
    if not request.session.get('userid', False):
        return HttpResponse("离开吧")
    if request.method == "POST":
        pk = request.POST.get("pk", None)
        if pk:
            try:
                jfp = jgz_huigun_php.objects.get(pk=pk)
            except Exception, e:
                return HttpResponse("pk(%s)不存:%s" % (pk, e))
            if jfp.state == "2":
                jiaoben = '/root/shell/php_faban_jgz.sh'
                ##request.session['userid']
                fa_hui = "2"
                one_id = one_uuid()
                t = multiprocessing.Process(target=sup_shell,
                                            args=(jiaoben, jfp.faban_id, request.session.get('userid', False),
                                                  one_id, fa_hui, "http://xxxx.xxx.com", "xxxxxx"
                                                  ))
                t.start()

                jgz_renwu.objects.create(faban_id=jfp.faban_id, state=jfp.state, jilu_log=one_id)
                jfp.state = 4
                jfp.save()
                return HttpResponse("任务已经生成uuid:%s" % one_id)
            elif jfp.state == "4":
                return HttpResponse("任务已经进入后台处理，详情查看任务记录")
            else:
                return HttpResponse("state参数不符，出大事，运维检测")



def xin_renwu(request):
    if request.session.get('userid', False):
        task_biaoji = request.GET.get("biaoji", None)
        task_biaoji = int(task_biaoji)
        sql = """
        SELECT t.id,t.faban_id,t.state,t.jilu_log,t.create_date from faban_jgz_renwu t
        WHERE t.state='%s'
            ORDER BY t.id desc

                    """ % task_biaoji
        tk = sql_select(sql)
        if task_biaoji == 1:
            task_biaoji = "发版记录"
        elif task_biaoji == 2:
            task_biaoji = "回滚记录"

        return render_to_response("jgz/renwu.html",
                                  {'daohangtiao': daohang(), 'tk': tk, 'task_biaoji': task_biaoji})

    return HttpResponse("out...")


def xin_renwuxiangqing(request):
    if request.session.get('userid', False):
        rw_xq_pk = request.GET.get('renwuxiangqing', None)
        try:
            rw_xq = jgz_renwu.objects.get(pk=rw_xq_pk)
            rw_xq_file = rw_xq.jilu_log
        except:
            return HttpResponse("没有这个任务的标号记录:%s" % rw_xq_pk)
        if rw_xq:
            f_file = "/root/" + rw_xq_file
            try:
                s = []
                f_uuid = open(f_file)
                for i in f_uuid:
                    s.append(i)
                return render_to_response('renwuxiangqing.html', {'s': s, 'daohangtiao': daohang()})
            except:
                s = "没找到这个UID文件"
                return render_to_response('renwuxiangqing.html', {'s': s, 'daohangtiao': daohang()})

    return HttpResponse("None")



#生成唯一的任务ID..
def one_uuid():
    one = ''.join(str(uuid.uuid1()).split('-'))
    return one




    
def daohang():
    leixings = sql_select("""
       SELECT weixin_leixing.name,  weixin_zhuji_duankou.name,weixin_zhuji_duankou.url_address
        from weixin_leixing JOIN weixin_zhuji_duankou
        ON
        weixin_leixing.id = weixin_zhuji_duankou.leixing_id_id
        ORDER BY  weixin_zhuji_duankou.create_date

    """)
    #{t1:java,ip: [[1,'url'],[2,'url']]}
    #得到想要的数据结构
    leixing_zidian = {}
    for i in leixings:
        if leixing_zidian.get(i[0],None):
            leixing_zidian[i[0]].append(i)
        else:
            leixing_zidian[i[0]]=[]
            leixing_zidian[i[0]].append(i)

    return leixing_zidian


def sql_select(sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows






















