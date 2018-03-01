#!/bin/bash
#
#check_wildfly_master_slave.sh
#检查java主从数据是否一致
#2015.11.24
#

url_log="/usr/local/nagios/libexec/url_log"
wrong_slve=""
isok="ok"

curl 'http://202.104.208.170:11280/solr/newchannel/replication?command=details&wt=json' -o $url_log -s
master_indexversion=`egrep -i -o --color=auto '"isMaster":"true","isSlave":"false","indexversion":[0-9]{0,}' $url_log | awk -F: '{print $NF}'`
slave12_indexversion=`egrep -i -o --color=auto '"isMaster":"false","isSlave":"true","indexversion":[0-9]{0,}' $url_log | awk -F: '{print $NF}'`

curl 'http://202.104.208.170:12780/solr/newchannel/replication?command=details&wt=json' -o $url_log -s
#master_indexversion=`egrep -i -o --color=auto '"isMaster":"true","isSlave":"false","indexversion":[0-9]{0,}' $url_log | awk -F: '{print $NF}'`
slave27_indexversion=`egrep -i -o --color=auto '"isMaster":"false","isSlave":"true","indexversion":[0-9]{0,}' $url_log | awk -F: '{print $NF}'`

if [[ $master_indexversion -ne $slave12_indexversion ]];then
	isok="not ok"
elif [[ $master_indexversion -ne $slave27_indexversion ]];then
	isok="not ok"
fi

result="master_newchannel:$master_indexversion slave12_newchannel:$slave12_indexversion slave27_newchannel:$slave27_indexversion"

if [[ "$isok" == "ok" ]];then
	echo "OK $result"
	exit 0
else
	echo "CRITICAL $result"
	exit 2
fi
