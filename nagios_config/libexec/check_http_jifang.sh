#!/bin/bash

BINPATH=/usr/local/nagios/libexec
cd $BINPATH
statusstr=''
hostname=''
STA=0
for host in www help zx m erp store seller crm
do
	statusstr=`./check_http -H ${host}.meilele.com -I 114.67.59.203`
	state=$?
	if [ $state -ne 0 ];then
		hostname="$hostname $host"
		STA=$state
	fi
done
if [ $STA -ne 0 ];then
	echo "${hostname} ${statusstr} $STA"
	exit $STA
else
	echo "ALL ${statusstr} $STA"
	exit 0
fi


#./check_http -H www.meilele.com -I 114.67.59.203