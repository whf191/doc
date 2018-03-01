#coding=utf-8
from django.shortcuts import render_to_response,HttpResponse,HttpResponseRedirect
from .models import phperror,manlog
import logging,json

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='phperror.log',
                filemode='a')


def put_phperror(request):
    if request.method == 'POST':
        log = request.POST.get("log", None)
        host = request.POST.get("host", None)
        url = request.POST.get("url", None)
        ip = request.POST.get("ip", None)
        cookie = request.POST.get("cookie", None)
        time = request.POST.get("time", None)
        project = request.POST.get("project", None)
        other = request.POST.get("other", None)
        log_type = request.POST.get("log_type", None)

        try:
            phperror_wirte = phperror(host=host, url=url, ip=ip, cookie=cookie,log=log,time=time,project=project,other=other,log_type=log_type)
            phperror_wirte.save()
        except Exception,e:
            return  HttpResponse(str(e))
        return HttpResponse("ok")

    return HttpResponse("not post")

def postmanlog(request):
    if request.method == 'POST':
        hostname = request.POST.get("hostname", None)
        msg = request.POST.get("msg", None)

        try:

            manlog_wirte = manlog(host=hostname, msg=msg)

            manlog_wirte.save()

            return HttpResponse("ok")

        except Exception, e:

            return HttpResponse("not ok %s" % str(e))


    return HttpResponse("not post")