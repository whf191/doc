#!/bin/bash
function run(){
   get_elas_pid = "ps -ef | grep elasticsearch | grep -v grep |awk '{print $2}' "
   if (  $get_elas_pid -eq 0  )
   then
       kill -9 $ get_elas_pid
	   sleep(2)
	   su es -c '/usr/local/elasticsearch-2.2.0/bin/elasticsearch' 
   else
       su es -c '/usr/local/elasticsearch-2.2.0/bin/elasticsearch' 
   fi
   
   
}

run()
