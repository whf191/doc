#!/bin/bash
#
#check_elk_log.sh
#2016.05.30
#

if [[ $# -ne 1 ]]
then
    echo -e "\e[1;31merror argument. use example \"$0 hostname\"\e[0m"
    exit 1
fi

hosts="server11 server12 zxback server14 memcached server16 server17 Server25 server19 Server20 Server21 Server24 www server26 Server27 server28 server29 server30 server31 server36 server38 server39 prod server42 server46"
hostname=$1

if [[ `echo $hosts | grep -c $hostname` -eq 1 ]]
then
    tmpfile=`mktemp`
    timeFive=`awk 'BEGIN{print strftime("%Y-%m-%dT%H:%M:%S",(systime()-300))}'`
    timeCurr=`awk 'BEGIN{print strftime("%Y-%m-%dT%H:%M:%S",(systime()))}'`
    timeTody=`awk 'BEGIN{print strftime("%Y-%m-%d",(systime()))}'`
    case $hostname in
        "Server25")
			curl -d "{\"query\":{\"filtered\":{\"query\":{\"term\":{\"@host\":\"${hostname}\"}},\"filter\":{\"and\":[{\"range\":{\"@timereported\":{\"gte\":\"${timeFive}\",\"lte\":\"${timeCurr}\",\"time_zone\":\"+08:00\"}}}]}}}}" http://202.104.208.170:9200/log_help_${timeTody}/_search -o $tmpfile -s
			;;		
      	"server46")
			curl -d "{\"query\":{\"filtered\":{\"query\":{\"term\":{\"@host\":\"${hostname}\"}},\"filter\":{\"and\":[{\"range\":{\"@timereported\":{\"gte\":\"${timeFive}\",\"lte\":\"${timeCurr}\",\"time_zone\":\"+08:00\"}}}]}}}}" http://202.104.208.170:9200/log_help_${timeTody}/_search -o $tmpfile -s
			;;
        *)
			curl -d "{\"query\":{\"filtered\":{\"query\":{\"term\":{\"@host\":\"${hostname}\"}},\"filter\":{\"and\":[{\"range\":{\"@timereported\":{\"gte\":\"${timeFive}\",\"lte\":\"${timeCurr}\",\"time_zone\":\"+08:00\"}}}]}}}}" http://202.104.208.170:9200/log_es_${timeTody}/_search -o $tmpfile -s
			;;
	esac
    count=`cat $tmpfile | egrep -o '\"hits\":\{\"total\":[0-9]+,\"max_score\":' | cut -d '"' -f 5 | cut -d ':' -f 2 | cut -d ',' -f 1`
    if [[ $count -gt 0 ]]
    then
        echo "OK $hostname $timeFive - $timeCurr total:$count | total=${count};"
        rm -rf $tmpfile
        exit 0
    else
        echo "CRITICAL $hostname $timeFive - $timeCurr | total=${count};"
        rm -rf $tmpfile
        exit 2
    fi
else
    echo -e "\e[1;31merror hostname \"$hostname\"\e[0m | total=${count};"
    exit 2
fi
