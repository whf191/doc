#coding=utf-8
from __future__ import unicode_literals
from django.shortcuts import HttpResponse,HttpResponseRedirect,render_to_response
import  os,json,uuid,subprocess
import get_token,requests,sys
from .models import *
from django.db import connection
faban_models = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(faban_models)
from faban.models import  faban_upload
from collections import OrderedDict


if not os.name == 'nt':
    from WXBizMsgCrypt import WXBizMsgCrypt

def home(request):
    sEncodingAESKey = 'y6O5GHnqzriyJAVHx2MEvs1nBdgQRWlvlsIMrnbLJyR'
    sToken = 'OkSEEEo3Qzjwbg8dCrcmaCpsRmopUhD'
    sCorpID = 'wx512775916d2936ff'
    wxcpt = WXBizMsgCrypt(sToken,sEncodingAESKey,sCorpID)
    #微信初始化认证
    if request.method == 'GET':
        # if request.GET.get('code') and request.GET.get('state') == 'w':
        #     rs = get_token.get_auth_code(request.GET.get('code'))
        #     #return HttpResponse('auth ,,,jiemian...%s' % rs)
        #     return HttpResponseRedirect("/?jsapi=wan")
        # elif request.GET.get('jsapi') == 'wan':
        #     return render_to_response("index.html")

        # sEncodingAESKey = 'y6O5GHnqzriyJAVHx2MEvs1nBdgQRWlvlsIMrnbLJyR'
        # sToken = 'OkSEEEo3Qzjwbg8dCrcmaCpsRmopUhD'
        # sCorpID = 'wx1d422f41ba7a2904'
        # wxcpt = WXBizMsgCrypt(sToken,sEncodingAESKey,sCorpID)

        v_signature = request.GET.get('msg_signature',None)
        v_TimeStamp = request.GET.get('timestamp',None)
        v_nonce     = request.GET.get('nonce',None)
        v_echostr   =  request.GET.get('echostr',None)
        ret,sEchoStr = wxcpt.VerifyURL(v_signature,v_TimeStamp,v_nonce,v_echostr)
        print ret,sEchoStr
        return HttpResponse(sEchoStr)

def weixin(request):
    if request.session.get('userid',None):
        return render_to_response("wx/index.html",{"daohangtiao":daohang()})
    WEIXIN_USRE_URL  = 'https://qyapi.weixin.qq.com/cgi-bin/user/getuserinfo?access_token=%s&code=%s'
    code = request.GET.get('code',None)
    print code,"+++++++++++++++++++++"
    if code is None:
        return HttpResponse(u"亲,你离开吧...")

    ACCESS_TOKEN = get_token.get_token_in_time()
    print ACCESS_TOKEN,"_____________"
    WEIXIN_USRE_URL = WEIXIN_USRE_URL % (ACCESS_TOKEN,code)
    weixin_userid = requests.get(WEIXIN_USRE_URL)
    print weixin_userid
    admin_group = ['wanwan','1','lilin']
    weixin_userid = weixin_userid.json()
    print weixin_userid
    print  weixin_userid.get('UserId',None)
    if weixin_userid.get('UserId',None) in admin_group:
        request.session['userid'] = weixin_userid.get('UserId',None)
        print request.session['userid'],"kkkkkkkkkkkkkk"
        print daohang()
        return render_to_response("wx/index.html",{"daohangtiao":daohang()})
    else:
        return HttpResponse(u"亲,ID:%s - - || 你不是运维管理中心的授权用户" % weixin_userid.get('UserId',None) )


def java8686(request):
    if os.name == 'nt':
        request.session['userid']=True

    if request.session.get('userid',None):
        leixing_type=request.GET.get('type',None)
        leixing_port = request.GET.get('port',None)

        if not (leixing_type and leixing_port):
            return HttpResponse(u"类型或端口为空..leixing_type:%s leixing_port:%s" % (leixing_type,leixing_port) )
        print "session:%s..laile..." % request.session.get('userid',None)
        sql = """
          SELECT weixin_leixing.name leixing , zhujiduankou.name duankou ,ip  from weixin_zhuji_duankou zhujiduankou
JOIN weixin_zhuji_duankou_zhuji_duankou_many  zjdkmany
ON
zhujiduankou.id=zjdkmany.zhuji_duankou_id
JOIN weixin_zhuji_ip  zip ON zip.id=zjdkmany.zhuji_ip_id
JOIN weixin_leixing ON weixin_leixing.id=zhujiduankou.leixing_id_id
WHERE zhujiduankou.name='%s' and  weixin_leixing.name='%s'

        """ % (leixing_port,leixing_type)
        zhixing_sql = sql_select(sql)
        print zhixing_sql
        leixing_duankou = "%s_%s" % (zhixing_sql[0][0],zhixing_sql[0][1])
        duankou_ip = [ i[-1] for i in zhixing_sql ]
        return render_to_response('wx/java8686.html',{'leixing_duankou':leixing_duankou,'duankou_ip':duankou_ip,'daohangtiao'
                                                   :daohang()})
    return HttpResponse('out')

def sql_select(sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows

def daohang():
    leixings = sql_select("""
       SELECT weixin_leixing.name,  weixin_zhuji_duankou.name,weixin_zhuji_duankou.url_address
        from weixin_leixing JOIN weixin_zhuji_duankou
        ON
        weixin_leixing.id = weixin_zhuji_duankou.leixing_id_id
        ORDER BY  weixin_leixing.name

    """)
    #{t1:java,ip: [[1,'url'],[2,'url']]}
    #得到想要的数据结构
    leixing_zidian = OrderedDict()
    for i in leixings:
        if leixing_zidian.get(i[0],None):
            leixing_zidian[i[0]].append(i)
        else:
            leixing_zidian[i[0]]=[]
            leixing_zidian[i[0]].append(i)

    return leixing_zidian

def shell(request):
    if os.name == 'nt':
        if request.method == 'POST':
            zhuji_ip = request.POST.get('zhuji',None)
            restart_off = request.POST.get('rf',None)
            leixing_duankou = request.POST.get('leixing_duankou',None)
            if zhuji_ip and restart_off and leixing_duankou:
                leixing,duankou = leixing_duankou.split('_')
                one_id = one_uuid()
                sql = """
       SELECT weixin_leixing.name leixing , zhujiduankou.name duankou ,ip ,zhujiduankou.jiaoben
   from weixin_zhuji_duankou zhujiduankou
            JOIN weixin_zhuji_duankou_zhuji_duankou_many  zjdkmany
            ON
            zhujiduankou.id=zjdkmany.zhuji_duankou_id
            JOIN weixin_zhuji_ip  zip ON zip.id=zjdkmany.zhuji_ip_id
            JOIN weixin_leixing ON weixin_leixing.id=zhujiduankou.leixing_id_id
                WHERE zhujiduankou.name='%s' and  weixin_leixing.name='%s' limit 1

                """ % (duankou,leixing)
                jiaoben = sql_select(sql)[0][-1]

                if not check_jiaoben(jiaoben):
                    return HttpResponse(u"脚本名称不符:%s" % jiaoben)
                title = leixing_duankou + "_" + restart_off + "_" +  jiaoben

                if not create_task(one_id,title,"userid","1"):
                    return HttpResponse("任务创建失败...")

                #begin 进入调脚本环节了...

                return HttpResponse(u"主机:%s,动作:%s,类型:%s,端口:%s,脚本:%s,uuid:%s" % (zhuji_ip,restart_off
                                ,leixing,duankou,jiaoben,one_id))

        return HttpResponse("out....")

    if request.session.get('userid',None):
        if request.method == 'POST':
            zhuji_ip = request.POST.get('zhuji', None)
            restart_off = request.POST.get('rf', None)
            leixing_duankou = request.POST.get('leixing_duankou', None)
            if zhuji_ip and restart_off and leixing_duankou:
                leixing, duankou = leixing_duankou.split('_')
                one_id = one_uuid()
                sql = """
            SELECT weixin_leixing.name leixing , zhujiduankou.name duankou ,ip ,zhujiduankou.jiaoben
        from weixin_zhuji_duankou zhujiduankou
                 JOIN weixin_zhuji_duankou_zhuji_duankou_many  zjdkmany
                 ON
                 zhujiduankou.id=zjdkmany.zhuji_duankou_id
                 JOIN weixin_zhuji_ip  zip ON zip.id=zjdkmany.zhuji_ip_id
                 JOIN weixin_leixing ON weixin_leixing.id=zhujiduankou.leixing_id_id
                     WHERE zhujiduankou.name='%s' and  weixin_leixing.name='%s' limit 1

                     """ % (duankou, leixing)
                try:
                    jiaoben = sql_select(sql)[0][-1]
                except:
                    return HttpResponse("sql查询脚本错误..")
                if not check_jiaoben(jiaoben):
                    return HttpResponse(u"脚本名称不符:%s" % jiaoben)
                title = leixing_duankou + "_" + restart_off

                if not create_task(one_id, title, request.session['userid'],"1"):
                    return HttpResponse("任务创建失败...")

                # begin 进入调脚本环节了...
                if not is_jiaoben(jiaoben):
                    return HttpResponse("脚本:%s不存在，任务取消" % jiaoben)

                subprocess.call("nohup %s %s %s %s %s &" % (jiaoben,request.session['userid'],restart_off,zhuji_ip,one_id),shell=True)


                return HttpResponse(u"主机:%s,动作:%s,类型:%s,端口:%s,脚本:%s,uuid:%s 调用成功 \n 进度，前往任务记录" % (zhuji_ip, restart_off
                                                                                , leixing, duankou, jiaoben, one_id))

        return HttpResponse("out.......")
    return HttpResponse("out...")

def renwu(request):
    if request.session.get('userid',False):
        task_biaoji = request.GET.get("biaoji",None)
        task_biaoji =  int(task_biaoji)
        sql="""
        SELECT t.task_id , t.title,t.context,t.username,t.task_zhuangtai,t.task_time from weixin_task t WHERE t.task_biaoji='%s'
ORDER BY t.task_time desc
        """  % task_biaoji
        tk = sql_select(sql)
        if task_biaoji == 1:
            task_biaoji = "重启记录"
        elif task_biaoji  == 2:
            task_biaoji  = "发版记录"
        elif task_biaoji == 3:
            task_biaoji  = "回滚记录"
        else:
            task_biaoji = "任务记录"

        return render_to_response("wx/renwu.html",{'daohangtiao':daohang(),'tk':tk,'task_biaoji':task_biaoji})

    return HttpResponse("out...")



def renwuxiangqing(request):
    if  request.session.get('userid',False):
        rw_xq = request.GET.get('renwuxiangqing',None)
        if rw_xq:
            f_file = "/root/" + rw_xq
            try:
                s = []
                f_uuid = open(f_file)
                for i in f_uuid:
                    s.append(i)
                return render_to_response('wx/renwuxiangqing.html',{'s':s,'daohangtiao':daohang()})
            except:
                s = "没找到这个UID文件"
                return render_to_response('wx/renwuxiangqing.html',{'s':s,'daohangtiao':daohang()})

    return HttpResponse("None")













#生成唯一的任务ID..
def one_uuid():
    one = ''.join(str(uuid.uuid1()).split('-'))
    return one
#脚本格式检查
def check_jiaoben(jiaoben):
    try:
        j = jiaoben.split('/')
        j = j[-1]
        j_name,j_sh = j.split('.')
        if j_sh == 'sh':
            return True
    except:
        return False

#脚本是否存在检查
def is_jiaoben(jiaoben):
    isjiaoben = os.path.isfile(jiaoben)
    if not isjiaoben:
        return False
    return True


#生成一个任务
def create_task(id,title,username,renwu_biaoshi):
    if id and title and username:
        try:
            t = task(task_id=id,title=title,username=username,task_biaoji=renwu_biaoshi)
            t.save()
            return True
        except:
            return False
    return False

def hello(request):
    return HttpResponse("hello")


#发送微信告警消息api
def send_weixin(request):
    if not (request.GET.get('wxzh',None)):
        wxzh = "@all"
    else:
        wxzh = request.GET.get('wxzh',None)

    if request.GET.get("content",None):
        content = request.GET.get("content",None)
        data = """ {"touser":"%s","msgtype":"text","agentid":1,"text":{"content":"%s",}}""" % (wxzh, content)
        ACCESS_TOKEN = get_token.get_token_in_time()
        r = requests.post(url="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s" % ACCESS_TOKEN, data=data)
        return HttpResponse("success")
    return HttpResponse("fail:message is null...")


###移动端发版代码..............

def php_faban(request):
    if request.session.get('userid',False):
        if request.method == "GET":
            t_in = ['php','java']
            t = request.GET.get('t',None)
            f = request.GET.get('f', None)
            if not (t in t_in):
                return HttpResponse("没有发版类型，out...")
            if not f:
                return HttpResponse("发版or回滚参数错误")

            if f == "1":
                sql = """
                     SELECT faban_faban_upload.id,faban_faban_types.name ,faban_fu_faban_type.name as fuleixing,faban_faban_upload.shenhe from faban_faban_upload
                JOIN faban_faban_types  ON  faban_faban_upload.faban_types_id_id=faban_faban_types.id
                JOIN  faban_fu_faban_type  ON faban_fu_faban_type.id=faban_faban_types.fu_faban_type_ids_id
                WHERE faban_faban_upload.shenqing in ('2','3')  AND faban_faban_upload.shenhe in ("0","1")   AND faban_fu_faban_type.name='%s'
                """ % t
                faban_list = sql_select(sql)
                t = t + "发版"
                return render_to_response('wx/phpfaban.html', {'daohangtiao': daohang(), 'faban_list': faban_list,'t':t,'f':f})
            elif f=="2":
                sql =  """
                     SELECT faban_faban_upload.id,faban_faban_types.name ,faban_fu_faban_type.name as fuleixing,faban_faban_upload.shenhe from faban_faban_upload
                JOIN faban_faban_types  ON  faban_faban_upload.faban_types_id_id=faban_faban_types.id
                JOIN  faban_fu_faban_type  ON faban_fu_faban_type.id=faban_faban_types.fu_faban_type_ids_id
                WHERE faban_faban_upload.shenqing in ('4','5')   AND faban_faban_upload.shenhe in ("0","1")  AND faban_fu_faban_type.name='%s'
                """ % t
                faban_list = sql_select(sql)
                t = t + "回滚"
                return render_to_response('wx/phpfaban.html', {'daohangtiao': daohang(), 'faban_list': faban_list, 't': t,'f':f})
            else:
                return HttpResponse("参数错误,out......")

        if request.method == "POST":
            pk = request.POST.get('pk', None)
            leixing = request.POST.get('leixing', None)
            fa_hui = request.POST.get('fa_hui', None)
            if pk and leixing:
                try:
                    pk = int(pk)
                except Exception, e:
                    print e
                    return HttpResponse("亲，离开吧...")
                if fa_hui == "1":
                    shenqing_id = "2"
                elif fa_hui == "2":
                    shenqing_id = "4"
                else:
                    return HttpResponse("参数不对，不执行")
                sql2 = """
                 SELECT faban_faban_upload.id,faban_faban_types.name , faban_fu_faban_type.name,faban_faban_upload.upfile,
                  faban_faban_upload.shijiancuo,faban_faban_types.jiaoben
                  from faban_faban_upload
    JOIN faban_faban_types  ON  faban_faban_upload.faban_types_id_id=faban_faban_types.id
	JOIN faban_fu_faban_type ON faban_fu_faban_type.id = faban_faban_types.fu_faban_type_ids_id
    WHERE faban_faban_upload.shenqing='%s'  AND  faban_faban_upload.id='%s'
      """ % (shenqing_id,pk)

                exec_sql = sql_select(sql2)
                if len(exec_sql) == 0:
                    return HttpResponse("没有发版任务")
                # 创建任务编号
                one_id = one_uuid()
                exec_sql= exec_sql[0]
                ID = exec_sql[0]
                YINGYONG = exec_sql[1]
                TYPE = exec_sql[2]
                UPFILE = exec_sql[3]
                SHIJIANCUO=exec_sql[4]
                jiaoben = exec_sql[5]
                #if not is_jiaoben(jiaoben):
                #    return HttpResponse("脚本不合法，out...")

                if TYPE == "php":
                    #fa_hui 为1表示正常发版，2表示回滚
                    if fa_hui == "1":
                        subprocess.call(
                            "nohup %s %s %s %s %s  %s %s &" % (jiaoben,ID ,YINGYONG,UPFILE,one_id,SHIJIANCUO,fa_hui),
                            shell=True)
                        #更改发版状态,把发版记录，写入数据库，2表示发版记录，3回滚记录
                        genggai_zhuangtai(pk,one_id,YINGYONG,2,3)
                        return HttpResponse("版本发了")
                    elif fa_hui == "2":
                        subprocess.call(
                            "nohup %s %s %s %s %s  %s %s &" % (
                                jiaoben, ID, YINGYONG, UPFILE, one_id, SHIJIANCUO, fa_hui),
                            shell=True)
                        genggai_zhuangtai(pk, one_id, YINGYONG, 3,5)
                        return HttpResponse("版本回滚了")

                    else:
                        return HttpResponse("参数错误，out....")
                elif TYPE == "java":
                    pass
                else:
                    return HttpResponse("不支持的发版类型%s" % TYPE)

            else:
                return HttpResponse("参数不完成,out...")

    else:
        return HttpResponse("out...")



def genggai_zhuangtai(pk,one_id,leixing,biaoji,shenqing):
    # 更改发版状态..shenqing表示 3表示正常发版 5表示回滚版本
    f_up = faban_upload.objects.get(pk=pk)
    f_up.shenqing = shenqing
    #发版审核按钮，不管是审核还是回滚，按钮状态只能是1,确认成功后的按钮是2
    f_up.shenhe = "1"
    username = f_up.faban_user.username
    f_up.save()
    create_task(one_id, leixing, username, biaoji)