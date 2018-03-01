#!/bin/bash
#2015.5.6 检查线上数据库数据备份是否成功

current_day=`date +%w`
if [[ $current_day -lt 6 ]];then
        jiangeshijian=$((current_day+1))
        real_date=`date +%Y%m%d -d "$jiangeshijian days ago"`
elif [[ $current_day -eq 6 ]];then
       real_date=`date +%Y%m%d`
elif [[ $current_day -lt 6 ]];then
        real_date=`date +%Y%m%d -d "-1 days ago"`
fi
currTime=$real_date
#echo $currTime

chkstr="web_odbc_13_$currTime.tar.gz rule_update_db_13_$currTime.tar.gz meilele_data_view_13_$currTime.tar.gz common_data_13_$currTime.tar.gz webdata_enwen_${currTime}00.tar.gz"

alive_str=""
dead_str=""
count=0
num=0
for i in ${chkstr}
do
        let "count++"
        if [ -f /mnt/05data/$i ];then
                file_size=`du -sh /mnt/05data/${i}|awk '{print $1}'`
                if [ "`du -k /mnt/05data/${i}|awk '{print $1}'`" -le "4" ];then
                        dead_str="$dead_str ${i}:${file_size}"
                        let "num++"
                else
                        alive_str="$alive_str ${i}:${file_size}"
                fi
        else
                let "num++"
                dead_str="$dead_str ${i}:nofile"

        fi
done

if [ $num -eq 0 ];then
        echo "OK all upload_success: $alive_str"
        exit 0
elif [ $num -gt 0 -a $num -lt $count ];then
                echo "CRITICAL upload_failed:$dead_str   upload_successful: $alive_str"
                exit 2
elif [ $num -eq $count ];then
                echo "CRITICAL all upload_failed: $dead_str"
                exit 2
fi
