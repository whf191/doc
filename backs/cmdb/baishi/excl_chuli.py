#coding=utf-8
from  __future__ import unicode_literals
import  xlrd
class read_excl(object):

    def __init__(self,fname):
        self.fname = fname
        self._read_open = self._open()

    def _open(self):
        bk = xlrd.open_workbook(self.fname)
        try:
            sh = bk.sheet_by_name("Sheet1")
            return sh
        except Exception,e:
            print e
            return False

    def get_rows(self,n=1):
        """  获取所有行数的数据，默认从第二行开始"""
        nrows = self._read_open.nrows
        row_list = []
        for i in range(n, nrows):
            row_data = self._read_open.row_values(i)
            row_list.append(row_data)
        return self.int_chuli(row_list)

    def int_chuli(self,row_list):
        """ 处理整个列表中的浮点为整数"""
        list2 = []
        if row_list:
            for  i in row_list:
                list2.append(map(self.int_map,i))
        return list2

    def int_map(self,x):
        """ 把浮点转整数"""
        if isinstance(x,float):
            return int(x)
        return x

if __name__ == '__main__':
    f = read_excl("moban111.xlsx")
    for i in  f.get_rows():
        print i


# bk = xlrd.open_workbook(fname)
# sheet_range = range(bk.nsheets)
#
# try:
#     sh = bk.sheet_by_name("Sheet1")
#
# except Exception,e:
#     print e
#
# #get 行数
# nrows = sh.nrows
#
# #get 列数
# ncols = sh.ncols
#
# row_list = []
#
# for i in range(1,nrows):
#     row_data = sh.row_values(i)
#     row_list.append(row_data)
#
# print  row_list













