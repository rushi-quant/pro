#!/bin/bash
# 不建议用这个更新
echo '删除脚本程序'
docker exec rsquant pkill -f python
echo '停止rsquant容器'
docker stop rsquant
echo '删除rsquant容器'
docker rm rsquant
echo '删除rsquant镜像'
docker rmi rsyuan/quant
echo '拉取rsquant镜像'
docker pull rsyuan/quant
echo '运行rsquant镜像'
docker run -itd --name rsquant --link rabbit --link mongo -p 9999:9999 rsyuan/quant
echo '启动行情服务器'
docker exec rsquant nohup python3 src/market.py config/market.json > /dev/null 2>&1 &
echo '启动策略服务器'
# nohup python3 src/server.py config/server.json 后台账号 后台密码 > /dev/null 2>&1 &
docker exec rsquant nohup python3 src/server.py config/server.json lszjl Zjl120221 > /dev/null 2>&1 &
echo '查看rabbit,mongo,rsquant容器'
docker ps
echo '查看python脚本'
ps -ef | grep python