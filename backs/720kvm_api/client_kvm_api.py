#coding=utf-8
import socket
HOST="192.168.0.51"
PORT=6789

class client_kvm_api(object):
    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.so = self._con()
        self.end = b"\r\n"

    def _con(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.so =  s.connect((self.host,self.port))
        return s
    def fasong(self,line):
        line = line + self.end
        self.so.sendall(line)
        print "发送成功，返回结果"
        print dir(self.so)
        print self.so.fileno
        data =  self.so.recv(65535)
        print data.decode("utf8").encode("utf8")

    def close(self):
        self.so.close()


