#!/bin/bash
str=`curl "http://crm.meilele.com/mllCRM/crmActionPullConfigController.do?TimedCrmClueLogMonitor" 2>/dev/null |sed 's#"##g' |sed 's#{##g' |sed 's#}##g'` 


interval=60
ruleCount=`echo $str |awk -F, '{print $1}' |awk -F: '{print $2}'`
updateTime=`echo $str |awk -F, '{print $2}' |awk -F "updateTime:" '{print $2}'`
newtime=`date -d "$interval minute ago"`
successCount=`echo $str |awk -F, '{print $3}' |awk -F: '{print $2}'`
intervaltime=$(($(date -d "$(echo $newtime)" "+%s")-$(date -d "$(echo $updateTime)" "+%s")))

#echo $newtime  $(date -d "$(echo $newtime)" "+%s") $updateTime $(date -d "$(echo $updateTime)" "+%s")
#echo $intervaltime

if [ ${#str} -eq 0 ];then
	echo "CRITICAL - check TimedCrmClueLogMonitor is null. "
	exit 2
#elif [ `date -d "$(echo $updateTime)" "+%s"` -gt `date -d "$(echo $newtime)" "+%s"` ] ;then
elif [ $intervaltime -gt 0 ] ;then	
	echo "CRITICAL - check TimedCrmClueLogMonitor is not run in $(($(($intervaltime/60))+$interval)) minutes. [$str] "
	exit 2

#{"ruleCount":44,"updateTime":"2017-08-04 08:45:00","successCount":44}
elif [ $(($ruleCount - $successCount)) -lt 5 ];then
		echo "OK - [$str] ."
		exit
else
	echo "CRITICAL - [$str] ."
	exit 2
fi
