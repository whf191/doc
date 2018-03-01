#/usr/bin/python
#coding=utf-8
import requests
import sys

def jiankong(cdn_list):
    error_cdn_list = []
    for i in cdn_list:
        get_url = requests.get(i)
        if  get_url.status_code != 200:
            error_cdn_list.append(str(get_url))

    if  len(error_cdn_list) == 0:
        print "img00[1-5] check status ok"
        sys.exit(0)
    else:
        print "img00[1-5] check status not ok -->" + "_".join(error_cdn_list)
        sys.exit(2)

if __name__ == '__main__':

    url_moban =  'http://img00%d.mllres.com/images/201709/1506648310401557472.jpg'
    cdn_list = [ url_moban % i for i in range(1,6)]
    jiankong(cdn_list)
