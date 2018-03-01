#coding=utf-8
import pycurl
input_url = "http://www.meilele.com/hongbao/?from=menu"

class Test:
    def __init__(self):
        self.contents = ''

    def body_callback(self, buf):
        self.contents = self.contents + buf


c = pycurl.Curl()
t = Test()
c.setopt(pycurl.WRITEFUNCTION, t.body_callback)
c.setopt(pycurl.ENCODING, 'gzip')
c.setopt(pycurl.URL, input_url)
c.perform()
http_code = c.getinfo(pycurl.HTTP_CODE)
http_conn_time = c.getinfo(pycurl.CONNECT_TIME)
http_pre_tran = c.getinfo(pycurl.PRETRANSFER_TIME)
http_start_tran = c.getinfo(pycurl.STARTTRANSFER_TIME)
http_total_time = c.getinfo(pycurl.TOTAL_TIME)
http_size = c.getinfo(pycurl.SIZE_DOWNLOAD)

htt_response_code = c.getinfo(pycurl.RESPONSE_CODE)
print 'http_code http_size conn_time pre_tran start_tran total_time'
print "%d %d %f %f %f %f" % (http_code, http_size, http_conn_time, http_pre_tran, http_start_tran, http_total_time)
