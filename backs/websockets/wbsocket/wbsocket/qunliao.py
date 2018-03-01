#!/usr/bin/python
#coding=utf-8
from dwebsocket.decorators import accept_websocket
from django.shortcuts import  render_to_response,HttpResponse,HttpResponseRedirect
import threading,uuid,json
from collections import  OrderedDict
qunliao = OrderedDict()

def get_uuid():
    """
     生成用户唯一UID
    :return:
    """
    return str(uuid.uuid1())

def get_ql_user(request):
    """
    获取所有群聊用户接口
    :param request:
    :return:
    """
    pk =  request.GET.get("pk",None)
    if pk:
        print pk
        get_qunliao_key = [k for k in qunliao if k != pk]
        get_qunliao_key = json.dumps(get_qunliao_key)
        return HttpResponse(get_qunliao_key)

    get_qunliao_key = [k for k in qunliao ]
    get_qunliao_key  = json.dumps(get_qunliao_key)
    return HttpResponse(get_qunliao_key)


def ql(request):
    """
    群聊首页

    :param request:
    :return:
    """
    return render_to_response("ql/index.html")


@accept_websocket
def qlsocket(request):
    """
        群聊socket

    :param request:
    :return:
    """
    if request.is_websocket:
        #print qlsocket.accept_websocket,"ddddddddddddddddddddddd"
        lock = threading.RLock()
        u_uid = get_uuid()
        qunliao[u_uid] = request.websocket
        qunliao[u_uid].send(u_uid)
        try:
            lock.acquire()
            print dir(request.websocket)
            for message in request.websocket:
                if not message:
                    print "laile.................."
                    break

                #clients[0].send("server:" + message)
                result = message.decode("utf-8").encode("utf-8")
                ret_user,ret_content  = json.loads(result)
                ret_content = ret_content.encode("utf-8")
                qunliao[ret_user].send(ret_content)




        finally:
            del qunliao[u_uid]
            lock.release()
