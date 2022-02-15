#!/bin/bash
echo '正在删除rsyuan/quant镜像'
docker rmi rsyuan/quant
echo '删除镜像=>成功'
cd /www/wwwroot/rushi-quant/rushiquant
echo '正在生成rsyuan/quant镜像'
docker build -t rsyuan/quant .
echo '生成镜像=>成功'
echo '正在推送rsyuan/quant镜像'
docker push rsyuan/quant
echo '推送镜像=>成功'
echo '请及时更新脚本'
