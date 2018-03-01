#!/bin/bash
#
#check_chat_7070.sh
#??chat???7070??ie??
#20160408
#
cd /usr/local/nagios/libexec/node-v4.4.2-linux-x64/bin
node xmpp.js chata.meilele.com:7070
comond_true=$?

if [ $comond_true -eq 0 ];then
	echo "OK "
	exit 0
else
	echo "CRITICAL "
	exit 2
fi

