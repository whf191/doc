#!/bin/bash
#kill `ps -ef | grep uwsgi8000 | grep -v grep | awk '{print $2}'`
#sleep 1
pkill -9  uwsgi
sleep 3
nohup uwsgi /etc/uwsgi8000.ini &
