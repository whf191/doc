#!/usr/bin/python
# coding=utf-8
from docker import  APIClient as Client
import sys

class docker_api(object):
    """
        封装docker源api
    """

    def __init__(self, base_url):
        self.base_url = base_url
        self.cli = None
        self._conn()

    def _conn(self):
        cli = Client(base_url=self.base_url)
        self.cli = cli
        return self.cli

    def containers(self):
        """ 输出所有启动的容器信息"""
        return self.cli.containers()

    def create_container(self, image ,external_directory,hostname=None,name=None,container_mnt_directory="/mnt/data",network_disabled=True):
        """ 创建容器函数"""
        """ 端口绑定说明,prots=["外部映射的端口号"] ,
            port_bindings={内部端口:[外部端口 | ("192.168.1.2","prots里的外部端口")元组表示法用于多IP，绑定端口]}

        """
        """
        container = self.cli.create_container(image="centos6-ssh",ports=[1111],host_config=self.cli.create_host_config(
            port_bindings={22:('127.0.0.1',1111)}
             )
                ,name="ceshi1")"""

        container = self.cli.create_container(image=image, volumes=[container_mnt_directory],
                                                  network_disabled=network_disabled,hostname=hostname,name=name,

                                                  host_config=self.cli.create_host_config(
                                                                                    binds={external_directory: {
                                                                                        'bind': container_mnt_directory,
                                                                                        'mode': 'rw' }})
                                                  )


        container_id = container['Id']
        return container_id

    def start(self, ID):
        s = self.cli.start(container=ID)
        return True

    def stop(self, ID):
        container = self.cli.stop(ID)
        return True
    def __del__(self):
        try:
            self.cli.close()
        except Exception,e:
            print e
if __name__ == '__main__':

    d = docker_api("tcp://192.168.2.165:2375")
    for i in d.containers():
        for i2 in i:
            print i2, i[i2]

    # d.cli.stop("9cb033b9a15c527163de9ce5cadccb500f54fa07ca2cca44275fcdd891ac9d2")

