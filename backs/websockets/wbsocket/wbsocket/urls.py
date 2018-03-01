#coding=utf-8
"""wbsocket URL Configuration

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
from django.conf.urls import *
from django.contrib import admin
from django.shortcuts import render_to_response,RequestContext,HttpResponse
from dwebsocket.decorators import accept_websocket
import threading,time,qunliao


def base_view(request):
    if request.GET.get("pk",None):
        return render_to_response('new_index_server.html')

    return render_to_response('new_index.html')


clients = []
servers = []
def pclient(request):
    print clients,"feiji.........................."
    return HttpResponse(clients)





@accept_websocket
def echo(request):
    if request.is_websocket:
        lock = threading.RLock()
        try:
            lock.acquire()
            clients.append(request.websocket)
            for message in request.websocket:
                if not message:
                    break
                # for client in clients:
                #     client.send(message)
                try:
                    print "1111111111111111"
                    servers[0].send("clent:" + message)
                except:
                    clients[0].send("bu zai xian")
                print dir(request.websocket)
                print request.websocket.__module__

        finally:
            clients.remove(request.websocket)
            lock.release()

@accept_websocket
def serverecho(request):
    if request.is_websocket:
        lock = threading.RLock()
        try:
            lock.acquire()
            servers.append(request.websocket)
            for message in request.websocket:
                if not message:
                    break

                clients[0].send("server:" + message)

        finally:
            print "guanbi........................"
            servers.remove(request.websocket)
            lock.release()


urlpatterns = patterns('',
    # Example:
    url(r'^$', base_view),
    url(r'^echo$', echo),
    url(r'^serverecho', serverecho),
    url(r'^pclient',pclient),
    url(r'^ql/$',qunliao.ql),
    url(r'^qlsocket$',qunliao.qlsocket),
    url(r'^get_ql_user/$',qunliao.get_ql_user),


    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)