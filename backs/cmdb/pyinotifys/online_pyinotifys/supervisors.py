#coding=utf-8
"""
1.安装
pip  install supervisor

2.生成配置文件
echo_supervisord_conf > /etc/supervisord.conf

error:
  pkg_resources.DistributionNotFound: meld3>=0.6.5
解决方法：
进入/usr/lib/python2.6/site-packages/supervisor-3.3.1-py2.6.egg-info/requires.txt 将meld3 >= 0.6.5 这一行注释掉，再重新执行即可。
vi /usr/lib/python2.6/site-packages/supervisor-3.3.2-py2.6.egg-info/requires.txt

3.编写app1配置文件

[program:pyinotifys]
command=/usr/bin/python t1.py
directory=/root/PycharmProjects/untitled/pyinotifys
user=root

#参数解释:
pyinotifys 应用名称
command 启动命令
directory 程序目录
user 用户

4.启动
supervisord -c /etc/supervisord.conf  //启动supervisor

#默认会把添加的应用启动.

更多参数:
autostart=true  ;start at supervisord start (default: true)
autorestart=true  ;whether/when to restart (default: unexpected)
startsecs=3  ;number of secs prog must stay running ( def . 1)
stderr_logfile=/tmp/bandwidth_err.log  ;redirect proc stderr to stdout (default false) 错误输出重定向
stdout_logfile=/tmp/bandwidth.log  ;stdout log path, NONE  for  none; default AUTO, log输出

5.常用命令
supervisorctl [start,startus,stop] app




"""