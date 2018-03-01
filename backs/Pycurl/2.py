# -*- coding: utf-8 -*-

'a socket example which send echo message to server.'

# import socket
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 建立连接:
# s.connect(('192.168.20.40', 7777))
# # 接收欢迎消息:
# print s.recv(1024)
# for data in ['Michael', 'Tracy', 'Sarah']:
#     # 发送数据:
#     s.send(data)
#     print s.recv(1024)
# s.send('exit')
# s.close()


#
# f = open('hosts.txt')
#
# f2 =  f.readlines()
# f3 = [i.split() for i in f2]
#
#
# s = """  INSERT INTO `cmdb`.`idc_hosts` (
# 	`hostname`,
# 	`hostip`,
# 	`hostport`,
# 	`hostuser`,
# 	`hostspassword`,
# 	`idc_id_id`,
# 		`node`,
# 	`createdate`
# )
# VALUES
# 	(
# 		'%s',
# 		'%s',
# 		'%s',
# 		'%s',
# 		'%s',
# 		'%s',
# 		' ',
# 		NOW()
# 	); """
#
# for i in f3:
#     print s % (i[0],i[1],i[2],i[3],i[4],i[5])
#

import requests
#
# r = requests.get("http://192.168.0.17/get_start_docker/?pip='%s'" % '192.168.0.18')
# if  r.json() == "1":
#     print "zhen"
#

l=["a","c"]
username="wanhaifeng"
hostip='192.168.20.50'

host_cmd = "".join(l)
data = {"username": username, "hostip":hostip,"host_cmd":host_cmd}
l=[]
r2 = requests.post("http://192.168.0.17/post_log/",data=data)
print r2.text




import socket
s = socket.socket()
s.connect()


















