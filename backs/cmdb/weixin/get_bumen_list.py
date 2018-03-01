# coding=utf-8
import json

import requests

import get_token


rs_token = get_token.get_token_in_time()
print rs_token

# url = 'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token=%s&id=4' % rs_token
# 获取成员信息
# url = 'https://qyapi.weixin.qq.com/cgi-bin/user/simplelist?access_token=%s&department_id=1935&status=0'% rs_token

# 创建成员
#url = 'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=%s' % rs_token
# name = '陈阳'
# position = '售后专员'
# create_user = {
#     "userid": "chenyang",
#     "name": name,
#     "department": [1935],
#     "position": position,
#     "mobile": "18180751250",
#     "gender": "2",
#     "email": "chengy@sysa.com.cn"
#         }
# create_user = json.dumps(create_user,ensure_ascii=False)

#创建菜单列表
# url = 'https://qyapi.weixin.qq.com/cgi-bin/menu/create?access_token=%s&agentid=1' % rs_token
# #删除菜单
url = 'https://qyapi.weixin.qq.com/cgi-bin/menu/delete?access_token=%s&agentid=1' % rs_token


# create_caidan = {
#    "button":[
#        {
#            "type":"click",
#            "name":"获取帮助",
#            "key":"get_help"
#        },
#        {
#            "name":"常用功能",
#            "sub_button":[
#                #  {
#                #     "type":"view",
#                #     "name":"日志",
#                #     "url":"http://work.sysa.com.cn"
#                # },
#                {
#                    "type":"view",
#                    "name":"老nagios监控",
#                    "url":"http://indoor.meilele.com/nagios/cgi-bin/status.cgi?host=all&servicestatustypes=16&hoststatustypes=15"
#                }
#            ]
#       }
#    ]
# }
# create_caidan = json.dumps(create_caidan,ensure_ascii=False)

# get_url = requests.post(url, data=create_caidan)

# print get_url.text


