#!/bin/bash
#
#微信发红包会话是否存活:访问链接结果:1正常:2warning:3critical
#check_weixin_seesion.sh
#2016.06.08
#

tmpfile=`mktemp`
check_url="http://www.meilele.com/test.html?nagios=1"
curl $check_url -o $tmpfile -s
count=`cat $tmpfile`
if [[ $count -eq 1 ]]
then
    echo "OK $check_url result:$count | result=${count};"
    rm -rf $tmpfile
    exit 0
elif [[ $count -eq 2 ]]
then
    echo "warning $check_url | result=${count};"
    rm -rf $tmpfile
    exit 1
elif [[ $count -eq 3 ]]
then
    echo "CRITICAL $check_url | result=${count};"
    rm -rf $tmpfile
    exit 2
else
    echo "CRITICAL $check_url | result=${count};"
    rm -rf $tmpfile
    exit 2
fi
