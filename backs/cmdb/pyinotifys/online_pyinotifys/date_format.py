#!/usr/bin/pytohn
#coding=utf-8
import datetime

def get_ymd():
    """
    获取年月

    :return:
    """
    ymd = datetime.date.today()
    ymd = ymd.strftime("%Y%m")
    return ymd


def last_month():
    """
    获取上一个月

    :return:
    """

    date = datetime.datetime.today()
    year = date.year
    month = date.month
    day = date.day
    if month == 1:
        month = 12
        year -= 1
    else:
        month -= 1

    if day == 31 and month in (4, 6, 9, 11):
        day = 30
    if day > 28 and month == 2:
        day = 29 if year % 4 == 0 else 28

    if month <10:
        month = "0%d" % month

    return "%s%s"% (year,month)

if __name__ == '__main__':
    print last_month()