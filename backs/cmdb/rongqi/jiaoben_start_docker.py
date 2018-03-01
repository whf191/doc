#coding=utf-8
#!/usr/bin/python
import  json
import  requests
import os,sys
ip = os.popen(" ip addr | grep br0 | grep inet |awk '{print $2}'|awk -F/ '{print $1}' ")
ip = ip.read().strip()


rs = requests.get("http://192.168.1.31:8000/get_start_docker/?pip='%s'" % ip)

rs = rs.json()
if len(rs) == 0:
    print u"没有相关容器ID，退出"
    sys.exit(2)
print u"一共要启动%s个容器" % len(rs)
for i in rs:
    #启动容器
    rongqi_id = i[0][:12]
    static_ip = i[1]
    gw = "192.168.0.1"
    print u"容器%s开始启动" % rongqi_id
    os.system("docker start %s" % rongqi_id)
    #绑定静态IP
    print u"给容器%s绑定静态IP:%s" % (rongqi_id,static_ip)
    os.system("pipework br0 %s  %s/22@%s" % (rongqi_id,static_ip,gw) )
    print u"容器:%s静态IP:%s启动完毕" % (rongqi_id,static_ip)