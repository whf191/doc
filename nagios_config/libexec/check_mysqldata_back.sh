#!/bin/bash
#2015.5.6 检查线上数据库数据备份是否成功

currTime="`date +%Y%m%d`"
#chkstr="web_odbc_13_$currTime.tar.gz rule_update_db_13_$currTime.tar.gz rule_mldb_13_$currTime.tar.gz meilele_data_view_13_$currTime.tar.gz common_data_13_$currTime.tar.gz meilele_new_$currTime.tar.gz discuz_bbs_$currTime.tar.gz data_center_$currTime.tar.gz callcenter_$currTime.tar.gz opentaps_db_$currTime.tar.gz zx_new1023_$currTime.tar.gz openfire_$currTime.tar.gz"

#chkstr="web_odbc_13_$currTime.tar.gz rule_update_db_13_$currTime.tar.gz meilele_data_view_13_$currTime.tar.gz common_data_13_$currTime.tar.gz meilele_new_$currTime.tar.gz discuz_bbs_$currTime.tar.gz data_center_$currTime.tar.gz callcenter_$currTime.tar.gz opentaps_db_$currTime.tar.gz zx_new1023_$currTime.tar.gz openfire_$currTime.tar.gz"
chkstr="meilele_new_$currTime.tar.gz discuz_bbs_$currTime.tar.gz data_center_$currTime.tar.gz callcenter_$currTime.tar.gz opentaps_db_$currTime.tar.gz zx_new1023_$currTime.tar.gz openfire_$currTime.tar.gz app_openfire_$currTime.tar.gz app_bak_${currTime}05.tar.gz enwen_bak_${currTime}01.tar.gz"

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
