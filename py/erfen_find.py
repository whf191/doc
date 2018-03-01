#!/usr/bin/python
#coding=utf-8
__author__ = "wanwan"


l = range(100)

def find(n,left,right):
    """
    参数n是指要查的树
    参数left,right代表查找范围
    """

    if right -left == 1:
        return left + 1

    else:
        middle = (left + right) / 2

        new_n = middle

        if n <= new_n:
            print 1
            return find(n, left, middle)
        else:
            print 2
            return find(n, middle, right)



if __name__ == '__main__':

    x =  find(48,0,len(l))
    print "index is %s" % x
    print l[x]


