#!/bin/bash
#yum install bind-utils -y
ns=/usr/bin/nslookup
BINPATH=/usr/local/nagios/libexec

if [ $# -ne 1 ] ;then
	echo "Usage:$0 URL"
	exit 1
fi

if [ ! -e $ns ] ;then
	echo "The command (nslookup) is not available!"
	exit 1
fi
#url="/images/common/site/logo.png"

url="/images/common/site/hot.gif"
#sip=`${ns} $1 8.8.8.8 |grep . |tail -n 1 |awk '{print $2}'`

sip=`${ns} iduwvib.qiniudns.com 8.8.8.8 |grep . |tail -n 1 |awk '{print $2}'`

$BINPATH/check_http -H $1 -u ${url} -I ${sip}
exit $?