#!/bin/bash
echo "关闭容器"

docker ps | awk '{print $1}' |grep -v CONTAINER |xargs docker stop

echo "关闭结束"
