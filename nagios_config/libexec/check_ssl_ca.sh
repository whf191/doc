#!/bin/bash

if [ $# -ne 10 ]
then
	echo "Usage: $0 -I [ip address] -H [ADDRESS] -p [PORT] -w [warn time] -c [critical time]"
	exit 2
fi


while [[ $# -gt 0 ]]
do
	case "$1" in
		-H)
			shift
			host=$1
		;;
		-I)
			shift
			ip=$1
		;;
		-p)
			shift
			port=$1
		;;
		-w)
			shift
			wdate=$1
		;;
		-c)
			shift
			cdate=$1
		;;
	esac
	shift
done
#date -d"10 day ago 2015-04-01" +%Y-%m-%d

#$(date -d "-$i days" +%m-%d-%Y)-00.log

datestr=`date -d "$(echo | openssl s_client -connect ${ip}:${port} 2>/dev/null | openssl x509 -noout -dates |grep After |awk -F= '{print $2}')" "+%Y-%m-%d %H:%M:%S"`

wstr=$(date  -d "$wdate days ago $(date -d "$datestr" "+%Y-%m-%d %H:%M:%S" )" "+%s")
cstr=$(date  -d "$cdate days ago $(date -d "$datestr" "+%Y-%m-%d %H:%M:%S" )" "+%s")
nstr=$(date "+%s")

#echo $nstr new 
#echo $(date -d "$datestr" "+%s" )  datestr
#echo $cstr cstr 
#echo $wstr wstr 
if [ "${nstr}" -gt "${cstr}" ];then
	echo "CRITICAL  - Certificate '$host' expires in $(( ($(date -d "$datestr" +%s) - $(date +%s))/(24*60*60) )) day(s) (${datestr})."
	exit 2
elif [ "${nstr}" -gt "${wstr}" ];then
	echo "WARNING - Certificate '$host' expires in $(( ($(date -d "$datestr" +%s) - $(date +%s))/(24*60*60) )) day(s) (${datestr})."
	exit 1
else
	echo "OK - Certificate '$host' will expire on (${datestr})."	
	exit 0
fi



