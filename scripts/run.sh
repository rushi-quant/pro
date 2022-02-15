#!/bin/bash
# 打包脚本
# 同步src/aioquant/utils
# 同步src/rushi
# 同步src/main.py
# 同步src/market.py
# 同步src/server.py
# 同步src/update_config.py
rm -rf ../src/aioquant/*.py
rm -rf ../src/aioquant/platform
rm -rf ../src/datas
rm -rf ../src/markets
rm -rf ../src/strategy