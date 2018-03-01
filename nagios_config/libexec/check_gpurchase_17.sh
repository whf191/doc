#!/bin/bash
#
#check_wildfly_master_slave.sh
#检查java主从数据是否一致
#2015.11.24
#

url_log="/usr/local/nagios/libexec/url_log"
wrong_slve=""
isok="ok"

curl 'http://14.152.121.136:11780/solr/gpurchase/replication?command=details&wt=json' -o $url_log -s
master_indexversion=`egrep -i -o --color=auto '"isMaster":"true","isSlave":"false","indexversion":[0-9]{0,}' $url_log | awk -F: '{print $NF}'`
slave17_indexversion=`egrep -i -o --color=auto '"isMaster":"false","isSlave":"true","indexversion":[0-9]{0,}' $url_log | awk -F: '{print $NF}'`

if [[ $master_indexversion -ne $slave17_indexversion ]];then
        isok="not ok"
fi

result="master_gpurchase:$master_indexversion slave17_gpurchase:$slave17_indexversion"

if [[ "$isok" == "ok" ]];then
        echo "OK $result"
        exit 0
else
        echo "CRITICAL $result"
        exit 2
fi