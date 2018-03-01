#coding=utf-8
import requests,sys,json




if __name__ == '__main__':
    print  u"""
        开始创建容器了\n
        版本1.0.0
    """
    while True:
        #cmdn_url = "http//127.0.0.1:8000"
        cmdb_url = "http://192.168.0.17"
        zidian = {'shenqing_id':None,"ip_zu":None}
        f1 = raw_input(u"输入申请的ID号:")
        if f1 == "exit":
            sys.exit(2)
        is_shenqi_id = requests.get("%s/is_shenqing/%s" % (cmdb_url,f1))
        is_shenqi_id = str(is_shenqi_id.json()).strip()
        if is_shenqi_id == "2":
            print u"id存在，不能继续，退出"
            sys.exit(2)
        elif is_shenqi_id == "3":
            print u"申请ID不存在，退出"
            sys.exit(2)
        try:
            f2 = requests.get("%s/get_rongqi_type_shenqing_id/%s" % (cmdb_url,f1))
            f2 = f2.json()[0]
            print u"ID查询出来的结果是", f2, type(f2)
            zidian['shenqing_id'] = f2
            f3 = requests.get("%s/get_ip" % cmdb_url)

            f3 = f3.json()
            print u"部门名称,1->研发部门 2->架构部门 3->测试部门"

            for i in enumerate(f3):
                print i

            f4 = raw_input(u"选择未使用的ip组号:")
            f5 = f3[int(f4)]
            print u"你选择的%s" % f5
            zidian['ip_zu'] = f5
            f6 = requests.get("%s/create_rongqi/chaungjian/?cj=%s" % (cmdb_url,json.dumps(zidian)))

            print u"汇总%s" % zidian

        except IndexError,e:
            print e
            print u"你选择申请ID不存，请重新输出"
            continue
        except ValueError,e:
            print e
            print u"请输入数字"
            continue