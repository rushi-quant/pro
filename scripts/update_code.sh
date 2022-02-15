#!/bin/bash
echo '更新策略脚本程序'
echo '正在拉取最新代码'
docker exec rsquant git pull -f origin master
echo '更新最新代码成功'