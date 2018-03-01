#coding=utf-8
from __future__ import unicode_literals
from django.shortcuts import render,render_to_response,HttpResponse,HttpResponsePermanentRedirect
import get_token,requests,os
from .models import *
from collections import OrderedDict
import json,random
from excl_chuli import read_excl
from django.contrib.auth.decorators import login_required

daohangtiao = {'查询':[['','成绩','/chengji/']]}
daohangtiao = False
def baishi(request):

    # if request.session.get('baishiid',None):
    #     return render_to_response("2/index.html", {'daohangtiao': daohangtiao,'s_yonghu':request.session['baishiid']})

    WEIXIN_USRE_URL  = 'https://qyapi.weixin.qq.com/cgi-bin/user/getuserinfo?access_token=%s&code=%s'
    code = request.GET.get('code',None)
    if code is None:
        return HttpResponse(u"亲,你离开吧...")

    ACCESS_TOKEN = get_token.get_token_in_time('wxd95ea6e4e48f1701','oe8F2I62rACC6bOwDrFH1GaK5uj2aLcYr5RZZ2HwZcCoSf91EJdnW-tcdybDZUtu')
    WEIXIN_USRE_URL = WEIXIN_USRE_URL % (ACCESS_TOKEN,code)
    weixin_userid = requests.get(WEIXIN_USRE_URL)

    weixin_userid = weixin_userid.json()

    wx_id =   weixin_userid.get('UserId',None)

    s_yonghu = {}

    s_yonghu['wx_id'] = wx_id
    request.session['baishiid'] = s_yonghu


    try:
        jiazhang_id = jiazhang.objects.get(weixin_id=wx_id)
        jiazhang_name = jiazhang_id.name
        s_yonghu['jiazhang_name'] = jiazhang_name
        #判断这个家长，是不是老师
        if jiazhang_id.Notes == "laoshi":
            jiazhang_alias = jiazhang_id.alias
            try:
                u1 = User.objects.get(username=jiazhang_alias)
                fanzhuang_banji = u1.banji_set.all()
                get_xueshengs = []
                for i in fanzhuang_banji:
                    xs_s = xuesheng.objects.filter(banji_id=i.pk)
                    if len(xs_s)  == 0:
                        continue
                    else:
                        for i2 in xs_s:
                            get_xueshengs.append([i2.pk,i2.name])
                if len(get_xueshengs) != 0:
                    s_yonghu['laoshi']=get_xueshengs

            except:
                return HttpResponse("老师的家长别名一栏和登录账户名不一致，将无法获取学生信息")

        xueshengs = jiazhang_id.xuesheng_set.all()
        l2 = []
        if len(xueshengs) == 0:
            xueshengs = False
        for i in xueshengs:
            l3 = [i.pk,i.name]
            l2.append(l3)

        s_yonghu["xuesheng"] = l2

    except:
        s_yonghu['jiazhang_name']=None
        return HttpResponse("你还未绑定学生，联系万老师处理")

    return HttpResponsePermanentRedirect("/chengji2/")
    return render_to_response("2/index.html",{'daohangtiao':daohangtiao,'s_yonghu':s_yonghu['jiazhang_name']})

def chengji(request):
    if request.session.get('baishiid', None):
        x_sheng = request.session.get('baishiid', None)['xuesheng']

        chengji_leixing = []
        if x_sheng:
            for i in x_sheng:
                xueshengs = {}
                xueshengs[i[1]] = []

                i_id = i[0]

                c_jibiao = chengjibiao.objects.filter(xuesheng_id=i_id).order_by("-pk")
                for i2 in c_jibiao:
                    cj_id = i2.pk
                    cj_leixing = i2.type_chengji_id.name
                    cj_s = [cj_id,cj_leixing]
                    xueshengs[i[1]].append(cj_s)
                chengji_leixing.append(xueshengs)


        return render_to_response("2/chengji.html",
                                  {'daohangtiao':daohangtiao,"chengji_leixing":chengji_leixing,
                                   's_yonghu':request.session.get('baishiid', None)['jiazhang_name']}
                                  )

    return HttpResponse("out...")

def chengji2(request):
    if request.session.get('baishiid', None):
        x_sheng = request.session.get('baishiid', None)['xuesheng']
        #return HttpResponse(x_sheng)
        #x_sheng = [["1","多多"]]
        if request.session.get('baishiid', None).get('laoshi',None):
            x_sheng = request.session.get('baishiid', None).get('laoshi',None)

        return render_to_response("2/chengji333.html",{'x_sheng':x_sheng,
        's_yonghu': request.session.get('baishiid', None)['jiazhang_name']
                                      })#

    return HttpResponse("out2...")

def cj_chaxun2(request):
    if not request.session.get('baishiid', None):
        return HttpResponse("out")
    #通过学生id，查询出所有学生的成绩类型
    pk = request.POST.get("pk",None)

    if pk:
        xueshengs = []
        c_jibiao = chengjibiao.objects.filter(xuesheng_id=pk).order_by("-pk")
        if len(c_jibiao) == 0:
            return HttpResponse("<p>老师还未录入你孩子的成绩</p>")
        for i2 in c_jibiao:
            cj_id = i2.pk
            cj_leixing = i2.type_chengji_id.name
            cj_s = [cj_id, cj_leixing]
            xueshengs.append(cj_s)
        anniu_yanse = ['btn-primary','btn-danger']


        get_xueshengs1 = ""
        get_xueshengs2 = """<button type="button" class="btn %s" id="chengji_bt1"
             onclick="cj_chaxun(%s)">%s</button> <br>"""
        for i in xueshengs:
            get_xueshengs1 = get_xueshengs1 + get_xueshengs2 % (suiji_yanse(anniu_yanse),i[0],i[1])


        return HttpResponse(get_xueshengs1)

    return HttpResponse("没有考试成绩类型")

#增加一个随机按钮的颜色方法
def suiji_yanse(anniu_yanse):
    return anniu_yanse[random.randint(0,1)]




def cj_chaxun(request):
    if not request.session.get('baishiid', None):
        return HttpResponse("out")
    pk = request.POST.get("pk",None)

    if pk:

        cjb = chengjibiao.objects.get(pk=pk)
        cj_zidian = OrderedDict()
        cj_zidian['yuwen'] = ["语文"]
        cj_zidian['shuxue']=["数学"]
        cj_zidian['yingyu'] = ["英语"]
        cj_zidian['zhengzhi'] = ["政治"]
        cj_zidian['lishi'] = ["历史"]
        cj_zidian['dili'] = ["地理"]
        cj_zidian['shengwu'] = ["生物"]
        cj_zidian['zongfen'] = ["总分"]
        cj_zidian['xiaozongfen'] = ["小总分"]
        cj_zidian['nianji_mingci'] = ["年级名次"]
        cj_zidian['banji_mingci'] = ["班级名次"]

        cj_zidian['yuwen'].append(cjb.yuwen)
        cj_zidian['shuxue'].append(cjb.shuxue)
        cj_zidian['yingyu'].append(cjb.yingyu)
        cj_zidian['zhengzhi'].append(cjb.zhengzhi)
        cj_zidian['lishi'].append(cjb.lishi)
        cj_zidian['dili'].append(cjb.dili)
        cj_zidian['shengwu'].append(cjb.shengwu)
        cj_zidian['zongfen'].append(cjb.zongfen)
        cj_zidian['xiaozongfen'].append(cjb.xiaozongfen)
        cj_zidian['nianji_mingci'].append(cjb.nianji_mingci)
        cj_zidian['banji_mingci'].append(cjb.banji_mingci)
        l2 = []
        for k,v in cj_zidian.items():
            if len(str(v[1]).strip()) != 0:
               l2.append("%s:%s   " % (v[0],v[1]) )

        return HttpResponse(" ".join(l2))
@login_required
def daoru(request):
    pk = request.GET.get("daoru_id",None)

    if pk:
        pldr = piliang_daoru.objects.get(pk=pk)

        cj_leixing_id = pldr.chengji_leixing.pk
        cj_leixing_id = type_chengji.objects.get(pk=cj_leixing_id)

        piliang_daoru_id = piliang_daoru.objects.get(pk=pk)


        excle_file =  pldr.excl_file
        excle_file = excle_file.__str__()
        if not is_jiaoben(excle_file):
            return HttpResponse("excle文件不存在:%s" % excle_file)

        cj_daoru_biaoshi = pldr.daoru_biaoshi

        f_excl = read_excl(excle_file)

        r_result = f_excl.get_rows()
        print r_result

        #真正的导入任务开始了.....
        for i2 in r_result:
            xuesheng_ids = i2[0]
            kaohao_id = i2[1]
            yuwen = i2[2]
            shuxue = i2[3]
            yingyu = i2[4]
            zhengzhi = i2[5]
            lishi = i2[6]
            dili = i2[7]
            shengwu = i2[8]
            zongfen =  i2[9]
            xiaozongfen = i2[10]
            nianji_mingci = i2[11]
            banji_mingci = i2[12]
            note = i2[13]

            #拿到考号
            get_kaohao = kaohao.objects.get(name=kaohao_id)

            #通过考号，找到学生
            xuesheng_obj = xuesheng.objects.get(kaohao_id=get_kaohao.pk)


            xuesheng_id = xuesheng_obj.pk

            cjb = chengjibiao.objects.create(xuesheng_id=xuesheng_obj, type_chengji_id=cj_leixing_id,
                        yuwen=yuwen, shuxue=shuxue, yingyu=yingyu, zhengzhi=zhengzhi,
                        lishi=lishi, dili=dili,
                        shengwu=shengwu, nianji_mingci=nianji_mingci,zongfen=zongfen,xiaozongfen=xiaozongfen,
                        banji_mingci=banji_mingci, Notes=note
                        )
            #cjb.save()

        piliang_daoru_id.daoru_biaoshi=1
        piliang_daoru_id.save()
        return HttpResponse("ok...")
@login_required
def daoru2(request):
    pk = request.GET.get("daoru_id", None)

    if pk:
        pldr = piliang_xuesheng_jiazhang_daoru.objects.get(pk=pk)

        banji_leixing_id = pldr.banji_leixing.pk
        #通过传过来的pk获取班级对象
        banji_leixing_id = banji.objects.get(pk=banji_leixing_id)

        piliang_daoru_id = piliang_xuesheng_jiazhang_daoru.objects.get(pk=pk)

        excle_file = pldr.excl_file
        excle_file = excle_file.__str__()
        if not is_jiaoben(excle_file):
            return HttpResponse(u"excle文件不存在:%s" % excle_file)

        cj_daoru_biaoshi = pldr.daoru_biaoshi

        f_excl = read_excl(excle_file)

        r_result = f_excl.get_rows()
        print r_result

        # 真正的导入任务开始了.....
        for i2 in r_result:
            kaohao_id = i2[0]
            jiazhang_name = i2[1]
            jiazhang_tel = i2[2]
            jiazhang_xingbie = i2[3]
            jiazhang_bieming = i2[4]
            jiazhang_weixin= i2[5]
            xuesheng_xingming = i2[6]
            xuesheng_xingbie = i2[7]
            xuesheng_xuehao = i2[8]

            # 检查考号，如果没有就创建，有，就更新
            try:
                kh_add = kaohao.objects.create(name=kaohao_id)
            except:
                kh_add = kaohao.objects.get(name=kaohao_id)
                kh_add.name = kaohao_id
                kh_add.save()

            #家长家长手机号，如果没有就创建，有，就更新
            try:
                jz_add = jiazhang.objects.create(tel=jiazhang_tel,name=jiazhang_name,
                xingbie=jiazhang_xingbie,alias=jiazhang_bieming,weixin_id=jiazhang_weixin)
            except:
                jz_add = jiazhang.objects.get(tel=jiazhang_tel)
                jz_add.name = jiazhang_name
                jz_add.xingbie = jiazhang_xingbie
                jz_add.alias = jiazhang_bieming
                jz_add.weixin_id = jiazhang_weixin
                jz_add.save()
                #jz_add = jiazhang.objects.update(tel=jiazhang_tel, name=jiazhang_name,
                #                        xingbie=jiazhang_xingbie, alias=jiazhang_bieming, weixin_id=jiazhang_weixin)

            #现在有了1.考号对象，家长对象，班级对象，开始学生和家长的绑定了
            try:
                t_xuesheng = xuesheng.objects.create(kaohao_id=kh_add,xuehao=xuesheng_xuehao,xingbie=xuesheng_xingbie
                                  ,name=xuesheng_xingming,banji_id=banji_leixing_id
                                )
            except:
                t_xuesheng = xuesheng.objects.get(kaohao_id=kh_add)
                t_xuesheng.xuehao=xuesheng_xuehao
                t_xuesheng.xingbie = xuesheng_xingbie
                t_xuesheng.name = xuesheng_xingming
                t_xuesheng.banji_id = banji_leixing_id
                t_xuesheng.save()

            #绑定家长
            t_xuesheng.jiazhang_id.add(jz_add)

        piliang_daoru_id.daoru_biaoshi = 1
        piliang_daoru_id.save()
        return HttpResponse("ok...")
    return HttpResponse("not ok...")






#脚本是否存在检查
def is_jiaoben(jiaoben):
    isjiaoben = os.path.isfile(jiaoben)
    if not isjiaoben:
        return False
    return True

def cj_zoushi_chaxun(request):
    if not request.session.get('baishiid', None):
        return HttpResponse("out")

    x_s= request.POST.get('xuesheng',None)
    k_m = request.POST.get('kemu',None)
    if not (x_s and k_m):
        return HttpResponse("没有你查询的数据")

    from .chengji_zhoushi import tu


    cjb = chengjibiao.objects.filter(xuesheng_id=x_s)
    if len(cjb) == 0:
        return HttpResponse("学生暂时还没有成绩，等待老师录入")
    cj_ty = ''
    cj_fenshu_str = ''
    for i in cjb:
        if eval("i.%s" % k_m):
            cj_ty += '\' %s \'' % i.type_chengji_id.name + ','
            cj_fenshu_str += eval("i.%s" % k_m) + ','

    cj_fenshu_head = '['
    cj_fenshu_tail =']'
    cj_fenshu = cj_fenshu_head + cj_fenshu_str + cj_fenshu_tail
    kemus=[
        ['yuwen','语文'],
        ['shuxue', '数学'],
        ['yingyu', '英语'],
        ['zhengzhi', '政治'],
        ['lishi', '历史'],
        ['dili', '地理'],
        ['shengwu', '生物']
    ]
    xz_kemu =''
    for i in kemus:
        if i[0] == k_m:
            xz_kemu = i[1]

    tu = tu % (cj_ty,xz_kemu,cj_fenshu)

    return HttpResponse(tu)

def cj_zhoushi(request):

    WEIXIN_USRE_URL  = 'https://qyapi.weixin.qq.com/cgi-bin/user/getuserinfo?access_token=%s&code=%s'
    code = request.GET.get('code',None)
    if code is None:
        return HttpResponse(u"亲,你离开吧...")

    ACCESS_TOKEN = get_token.get_token_in_time('wxd95ea6e4e48f1701','oe8F2I62rACC6bOwDrFH1GaK5uj2aLcYr5RZZ2HwZcCoSf91EJdnW-tcdybDZUtu')
    WEIXIN_USRE_URL = WEIXIN_USRE_URL % (ACCESS_TOKEN,code)
    weixin_userid = requests.get(WEIXIN_USRE_URL)

    weixin_userid = weixin_userid.json()

    wx_id =   weixin_userid.get('UserId',None)

    s_yonghu = {}

    s_yonghu['wx_id'] = wx_id
    request.session['baishiid'] = s_yonghu


    try:
        jiazhang_id = jiazhang.objects.get(weixin_id=wx_id)
        jiazhang_name = jiazhang_id.name
        # 判断这个家长，是不是老师
        if jiazhang_id.Notes == "laoshi":
            jiazhang_alias = jiazhang_id.alias
            try:
                u1 = User.objects.get(username=jiazhang_alias)
                fanzhuang_banji = u1.banji_set.all()
                get_xueshengs = []
                for i in fanzhuang_banji:
                    xs_s = xuesheng.objects.filter(banji_id=i.pk)
                    if len(xs_s) == 0:
                        continue
                    else:
                        for i2 in xs_s:
                            get_xueshengs.append([i2.pk, i2.name])
                if len(get_xueshengs) != 0:
                    s_yonghu['laoshi'] = get_xueshengs

            except:
                return HttpResponse("老师的家长别名一栏和登录账户名不一致，将无法获取学生信息")



        s_yonghu['jiazhang_name'] = jiazhang_name

        xueshengs = jiazhang_id.xuesheng_set.all()

        l2 = []
        if len(xueshengs) == 0:
            xueshengs = False
        for i in xueshengs:
            l3 = [i.pk,i.name]
            l2.append(l3)

        s_yonghu["xuesheng"] = l2

    except:
        return HttpResponse("你还未绑定学生，联系万老师处理")
        s_yonghu['jiazhang_name']=None

    xueshengs = s_yonghu["xuesheng"]
    if s_yonghu.get("laoshi", None):
        xueshengs = s_yonghu['laoshi']

    kemus=[
        ['yuwen','语文'],
        ['shuxue', '数学'],
        ['yingyu', '英语'],
        ['zhengzhi', '政治'],
        ['lishi', '历史'],
        ['dili', '地理'],
        ['shengwu', '生物']
    ]





    return render_to_response("2/chengji_zhoushi.html",{'s_yonghu':s_yonghu['jiazhang_name'],'kemus':kemus,'xueshengs':xueshengs})
@login_required
def xiazai(request):
    xiazai = request.GET.get("down",None)
    from django.utils.http import urlquote
    if xiazai:
        xiazai_name = xiazai.split("/")
        xiazai_name = xiazai_name[-1]
        xiazai = "update/" + xiazai
        try:
            response = HttpResponse()
            response['Content-Disposition'] = 'attachment;filename=%s' % urlquote(xiazai_name)
            f = open(xiazai,'r').read()
            response.write(f)
            return response
        except:
            return HttpResponse("文件不存在")


