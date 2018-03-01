#coding=utf-8
from docker import  APIClient as Client
from django.db import connection
import sys


def my_custom_sql(shenqing_id):
    """  获取申请的ID，容器类型，容器外部端口 """
    cursor = connection.cursor()
    cursor.execute("""
        select t.id,t2.rongqi_type from rongqi_shenqing_rongqi t JOIN
        rongqi_type_rongqi t2 ON t.type_rongqi_id_id=t2.id
        where t.id=%s and t.shenqing_status in (1,3)
        """ % shenqing_id )
    row = cursor.fetchall()
    return row

def get_ip_sql():
    """ 获取所有未实用的IP"""
    cursor = connection.cursor()
    cursor.execute("""
               select t.ip,t2.ip,t2.id ,t.ip_name from  rongqi_ipaddress_rongqi t JOIN  rongqi_pipaddress_rongqi t2
        ON
        t.pipaddress_rongqi_id_id=t2.id  WHERE t.is_enable=0
                """  )
    row = cursor.fetchall()
    return row

def get_start_pip(pip):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT rgr.rongqi_id , rir.ip , rpr.ip as pip from rongqi_guanli_rongqi rgr JOIN
        rongqi_ipaddress_rongqi rir

        ON
        rgr.rongqi_ip_id = rir.id
        JOIN
        rongqi_pipaddress_rongqi rpr
        ON
        rpr.id=rir.pipaddress_rongqi_id_id
        WHERE rpr.ip=%s
    """ % pip)
    row = cursor.fetchall()
    return row




class Docker_mll(object):
    """
        封装docker源api
    """

    def __init__(self,base_url):
        self.base_url = base_url
        self.cli = None
        self._conn()
    def _conn(self):
        try:
            cli = Client(base_url=self.base_url)
        except Exception,e:
            print e
            sys.exit(1)
        self.cli = cli
        return self.cli

    def containers(self):
        """ 输出所有启动的容器信息"""
        return self.cli.containers()

    def create_container(self,select_rongqi_ip,select_pip,select_rongqi_type,select_shenqing_id,external_directory):
        """ 创建容器函数"""
        """ 端口绑定说明,prots=["外部映射的端口号"] ,
            port_bindings={内部端口:[外部端口 | ("192.168.1.2","prots里的外部端口")元组表示法用于多IP，绑定端口]}

        """
        """
        container = self.cli.create_container(image="centos6-ssh",ports=[1111],host_config=self.cli.create_host_config(
            port_bindings={22:('127.0.0.1',1111)}
             )
                ,name="ceshi1")"""

        try:
            container = self.cli.create_container(image=select_rongqi_type,volumes=['/mnt/data'],network_disabled=True,host_config=self.cli.create_host_config(
                binds={external_directory:{
                    'bind':'/mnt/data',
                    'mode':'rw'

                }

                }


            ))


            container_id =  container['Id']
        except Exception,e:
            return False
        return container_id

    def start(self,ID):
        try:
            s = self.cli.start(container=ID)
        except Exception,e:
            return False
        return True

    def stop(self,ID):
        """停止容器"""
        try:
            container = self.cli.stop(ID)
        except Exception,e:
            print e
            return False
        return True
if __name__ == '__main__':

    d= Docker_mll("tcp://192.168.2.165:2375")
    for i in  d.containers():
        for i2 in i:
            print i2,i[i2]

    d.create_container(b = 1,a=3,port=33)
#d.cli.stop("9cb033b9a15c527163de9ce5cadccb500f54fa07ca2cca44275fcdd891ac9d2")