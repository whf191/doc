#!/usr/bin/python
#coding=utf-8

import os,json
class kvm_api(object):
    """
    kvm_api的方法,为了防止阻塞，用reactor.callInThread方法

    """
    def __init__(self,sendLine,fenge,logging,data):
        self.sendLine = sendLine
        self.fenge = fenge
        self.logging = logging
        self.data = data
        self.error = {"state":"false","msg":None}
        self.success = {'state':"success","msg":None}

    def kvm_list(self):
        read = os.popen("virsh list")
        read = read.read().strip().split("\n")[2:]
        read = [ i.split() for i in read]
        self.success['msg'] = read
        read = json.dumps(self.success)
        self.logging.info("kvm_list方法返回结果:%s" % read)

        self.sendLine(read + self.fenge)

    def kvm_dumpxml(self,kvm_rongiq_name):
        read = os.popen("virsh dumpxml %s" % kvm_rongiq_name)
        read = read.read().strip().split('\n')
        self.success['msg'] = read
        read = json.dumps(self.success)
        self.logging.info("kvm_dumpxml方法返回结果:%s" % read)
        self.sendLine(read + self.fenge)


    def run(self):
        try:
            data = json.loads(self.data)
            if data.get("kvm_list",None):
                self.kvm_list()
                return True
            if data.get("kvm_dumpxml",None):
                kvm_rongqi_name = data.get("kvm_dumpxml",None)
                self.kvm_dumpxml(kvm_rongqi_name)
                return True

            self.error["msg"] = "not cmd"
            self.sendLine(json.dumps(self.error))
            return True

        except Exception,e:
            self.error["msg"] = "not json"
            self.sendLine(json.dumps(self.error))
            return False