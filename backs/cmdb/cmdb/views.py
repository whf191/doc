# #coding=utf-8
# from  django.shortcuts import  HttpResponse,HttpResponsePermanentRedirect
# from django.contrib.auth import login
# from  django.contrib.auth.models import User
# import json,urllib
# #AES解密包部分
# from Crypto.Cipher import  AES
# import base64,requests,time
# """
# 用户中心接入，要修改 django源码 ,路径为
# from django.contrib.auth import login
#
# try:
#         request.session[BACKEND_SESSION_KEY] = user.backend
#     except:
#         request.session[BACKEND_SESSION_KEY] = 'django.contrib.auth.backends.ModelBackend'
#
# """
#
#
# GET_USER_EMAIL_URL="http://passport.meilele.com/dataauthority/getUserInfoByCode"
# def ml(request):
#     ln_tk = request.COOKIES.get('ln_tk',None)
#     if ln_tk is None:
#         return  HttpResponsePermanentRedirect("http://passport.meilele.com/login.jsp?redirect=http://py.meilele.com/ml/")
#     #ln_tk的url格式解码
#
#     ln_tk = urllib.unquote(ln_tk).strip()
#     ln_tk = base64.decodestring(ln_tk)
#     try:
#         ss = AES.new('abcdef0123456789',AES.MODE_CBC,'0123456789abcdef')
#         ss2 = ss.decrypt(ln_tk)
#     except Exception ,e:
#         print e
#         return HttpResponse(u"AES解密错误，联系管理员")
#
#     print ss2,type(ss2),repr(ss2[:-3]),repr(ss2)
#     aes_context_find = ss2.find("}") + 1
#     print aes_context_find
#     aes_context = ss2[:aes_context_find]
#     print aes_context
#     aes_context = json.loads(aes_context)
#
#     print
#     print aes_context
#     #通过userLoginCode去获取邮箱
#     userLoginCode = aes_context['userLoginCode']
#     try:
#         rg = requests.get(url=GET_USER_EMAIL_URL,params={'code':userLoginCode})
#         rg = rg.json()
#         if len(rg) == 0:
#             return HttpResponse(u"没获取到用户邮箱")
#     except:
#         return HttpResponse(u"不能访问用户中心认证.")
#
#     #通过用户中心用户插入一条记录到user用户表，用户中中心的用户，用户默认加把盐(yhz) - - ||
#     yhz_user = rg.get('userLoginCode',None)
#     yhz_user_name = rg.get('userName',None)
#     yhz_mail = rg.get('email',None)
#     if not (yhz_user and yhz_mail):
#         return HttpResponse(u"用户中心获取的用户或邮箱为空")
#
#     yhz_user= yhz_user + "_yhz"
#     yhz_user_name = yhz_user_name + "_yhz"
#     try:
#
#         users = User.objects.get(username=yhz_user)
#         l = login(request,users)
#         return HttpResponsePermanentRedirect('/admin/')
#
#     except Exception,e:
#         print e
#         pass
#     try:
#         user_into = User(password='pbkdf2_sha256$24000$famm2CyKofrY$HW8F4YTgbxybMQsCUmjIWZl1WDtZnYtgqCEMv0fwiHU=',
#                   is_superuser=0, username=yhz_user, first_name=yhz_user_name, last_name=yhz_user_name, email=yhz_mail,
#                   is_staff=1, is_active=1)
#         user_into.save()
#         l = login(request,user_into)
#         return HttpResponsePermanentRedirect('/admin/')
#
#     except Exception,e:
#             print e
#             return HttpResponse(u"添加用户中心用户，失败了..- -||")
#
