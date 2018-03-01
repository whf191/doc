#!/usr/bin/python
#coding=utf-8
import  urllib,json


def postlog(data,url="http://ywweixin.meilele.com/phperror/"):
    """
    post  方式提交...

    :param data:
    :param url:
    :return:
    """
    data = data
    data_cookie = data['cookie']
    data_other = data['other']
    data['cookie'] = json.dumps(data_cookie)
    data['other'] = json.dumps(data_other)

    parmas = urllib.urlencode(data)
    f = urllib.urlopen(url,parmas)
    return f.read()


def post_man_log(data,url):
    data = data
    parmas = urllib.urlencode(data)
    f = urllib.urlopen(url,parmas)
    return f.read()


if __name__ == '__main__':
        pass










