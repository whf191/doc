#!/bin/bash
#
#用于提醒证书过期
#2015.09.07
#check_certificate.sh
#邮箱服务器、后台客户端、后台服务器端、app服务器、内网规则

function countDate()    #计算还有多少天证书过期的函数
{
        expirationTime=$1       #证书过期时间
        currentTime=`/bin/date +%s -d"00:00:00"`        #当前时间
        diffTime=$(($(($expirationTime-$currentTime))/86400))   #距过期多少天
        echo $diffTime
}

declare -A item         #声明关联数组
item[mail]=$(countDate `/bin/date +%s -d"2017-08-04 00:00:00"`) #邮箱的过期时间
#item[help_client]=$(countDate `/bin/date +%s -d"2017-02-03 00:00:00"`)  #后台客户端的过期时间
#item[help_server]=$(countDate `/bin/date +%s -d"2017-12-22 00:00:00"`)  #后台服务器端的过期时间
#item[rule_client]=$(countDate `/bin/date +%s -d"2015-12-10 00:00:00"`) #规则客户端的过期时间 https://rengine.meilele.com:8081/data/login.jsp
#item[rule_server]=$(countDate `/bin/date +%s -d"2015-11-22 00:00:00"`) #规则服务器端的过期时间 https://rengine.meilele.com:8081/data/login.jsp
item[app]=$(countDate `/bin/date +%s -d"2019-06-29 00:00:00"`)  #app的过期时间 https://indoor.meilele.com:4443/down.html

T=""
F=""
isOK="YES"
for i in ${!item[*]}    #遍历关联数组下标
do
        if [[ ${item[$i]} -le 10 ]];then        #提前15天提醒是否过期
                isOK="NO"                                               #是否有快过期的
                F="$F $i:${item[$i]}天过期"             #记录下要过期的
        else
                T="$T $i:${item[$i]}天过期"             #记录下暂时不会过期的
        fi
done

if [[ $isOK == "YES" ]];then
        echo "OK $T"
        exit 0
else
        echo "Criticle 即将过期的:$F 暂未到期的:$T"
        exit 2
fi
