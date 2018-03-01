#!/usr/bin/python
#coding=utf-8
from SocketServer import ThreadingTCPServer, StreamRequestHandler
import traceback,os,threading,logging
from kvm_api import kvm_api

#进入到脚本本身目录..
os.chdir(os.path.split(os.path.realpath(__file__))[0])

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename=__file__+".log",
                filemode='a')


class MyStreamRequestHandlerr(StreamRequestHandler):

    def handle(self):
        #数据处理层while来维护客户端的socket长连接.
        logging.info(u"新的客户端建立连接..%s:%s" % self.client_address )
        while True:
            try:
                fenge = b"\r\n"
                data = self.rfile.readline().strip()
                #print "receive from (%r):%r" % (self.client_address, data)
                #print "一共有这么多线程%s" % threading.current_thread()
                kpi = kvm_api(self.wfile.write,fenge,logging,data)
                kpi.run()

                # huoqu = getattr(kpi,data,False)
                #print dir(self.connection)
                #print dir(self.request)

                # if not huoqu:
                #     self.wfile.write(data + "不是合法的数据" + fenge)
                #     logging.error(data + u"不是合法的数据")
                # else:
                #     logging.info(u"指令:%s验证成功,开始调用" % data )
                #     huoqu()
            except:
                logging.info(u"客户端断开了.%s:%s" % self.client_address)
                break

    def finish(self):
        #客户端断开后执行的操作.
        print "我是finish..."



class zdy_ThreadingTCPServer(ThreadingTCPServer):
    pass


if __name__ == "__main__":
    host = "0.0.0.0"
    port = 6789
    addr = (host, port)
    server = zdy_ThreadingTCPServer(addr, MyStreamRequestHandlerr)
    print "socket_server启动..."
    logging.info("socker_server 开始启动")
    server.serve_forever()