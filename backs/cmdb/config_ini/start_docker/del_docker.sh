#!/bin/bash
echo " 删除所有容器"

docker ps -a | awk '{print $1}' |grep -v CONTAINER |xargs docker   rm

echo "删除所有结束"
