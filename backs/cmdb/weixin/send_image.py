# coding=utf-8
import json

import requests

import get_token
import logging_01
import up_images


# nginx_png = '/home/linshi/copy_png/70_nginx.png'

def get_message(touser, nginx_png):
    # 获取上传图片的media_id
    rs_up_images = up_images.up_image(filename=nginx_png)
    media_id = rs_up_images.get("media_id", None)
    if media_id:

        image_message = {
    "touser": touser,
    "msgtype": "image",
    "agentid": 2,
    "image": {
        "media_id": media_id
    },
    "safe": "0"
}
        corp_id = 'wx1d422f41ba7a2904'
        Secret = 'Ta68AqynGlZiEaVRydONupS9Gd4A7uj2iMb2KONSrjSRd0DB4dwbc3rhP2JL7_VA'
        rs_token = get_token.get_token_in_time(corp_id, Secret)
        logging_01.log_jilu(info=u'发送图片模块，获取rs_token:' + str(rs_token))
        url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s' % rs_token
        get_url = requests.post(url, data=json.dumps(image_message))
        print get_url.text
    else:
        logging_01.log_jilu(critical='shibaila....meiyouqudao.meida_id')
if __name__ == '__main__':
    get_message('33', nginx_png)
