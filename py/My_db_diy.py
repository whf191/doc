#!/usr/bin/python
#coding=utf-8
__author__ = "wanwan"
import  os

os.chdir(os.path.dirname(__file__))

try:
    import cPickle as pickle
except:
    import pickle

class ConnectError(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg

class My_db_div_danlie(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(My_db_div_danlie,cls).__new__(cls, *args, **kwargs)
        return cls._instance


class My_db_diy(My_db_div_danlie):

    def __init__(self):
        self.db_diy_file = "db_diy_file.pk"
        self.obj = None
        self.db_init()
        self.connect()
    def _is_db_diy_file(self):
        return os.path.isfile(self.db_diy_file)

    def db_init(self):
        """
        Dict1 = {"users":[{},{}] }
        """
        if not self._is_db_diy_file():
            self.obj = {"users":[]}
            self.commit()

    def connect(self):
        if not self._is_db_diy_file():
            raise ConnectError("connect is faile,please runing db_init() ")
        else:
            db_file = open(self.db_diy_file,"rb")
            pload = pickle.load(db_file)
            db_file.close()
            self.obj = pload
            return self.obj

    def commit(self):
        db_file = open(self.db_diy_file,"wb")
        pdump = pickle.dump(self.obj,db_file)
        db_file.close()
        return pdump

    def _is_table(self,table):
        if table not in self.obj:
            return False
        else:
            return True

    def add(self,table, table_data):
        if not self._is_table(table):
            return False
        else:
            self.obj[table].append(table_data)
            return True

    def create_table(self,table):
        if table not in self.obj:
            self.obj[table] = []
            return True
        else:
            return False

    def all(self,table):
        try:
            datas = [ (k,v) for k,v in enumerate(self.obj[table])]
            return datas
        except Exception,e:
            print e
            return False

    def remove_index(self,table,index):
        if not self._is_table(table):
            return False
        else:
            return self.obj[table].remove(self.obj[table][index])


    def remove_table(self,table):
        if not self._is_table(table):
            return False
        else:
            del self.obj[table]
            return True


    def update_index(self,table,index,data):
        if not self._is_table(table):
            return False
        else:
            self.obj[table][index] = data
            return True

    def show_table(self):
        return self.obj.keys()


"""
例子说明:
  My_db_diy 类实例化后，会预创建个{"users":[]}对象
"""

#显示所有表

def show_table():
    my = My_db_diy()
    my.show_table()

#添加表

def add_table():
    my = My_db_diy()
    my.create_table("table1")
    my.commit()

#向表添加个数据

def add_data():
    my = My_db_diy()
    my.add("table1",{"a1":1,"a2":2})
    my.commit()

#删除表数据

def remove_data():
    my = My_db_diy()
    my.remove_index("table1",1)
    my.commit()

#查询表数据
def select():
    my = My_db_diy()
    return my.all("users")

#更新表数据
def update():
    my = My_db_diy()
    my.update_index("table1",1,{"t1":1})
    my.commit()




if __name__ == '__main__':
    print select()






