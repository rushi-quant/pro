# -- coding: utf-8 --
# cython: language_level=3
'''
@author:rushi
@version:1.0.0
@time:2022/1/7 21:54
'''
import sys
from aioquant import quant
from aioquant.configure import config
# 防止server closed
import nest_asyncio
nest_asyncio.apply()
def start():
    if len(sys.argv) >= 4:
        username = sys.argv[2]
        password = sys.argv[3]
        config.username = username
        config.password = password
        from strategy.server import Server
        Server()

if __name__ == '__main__':
    config_file = 'config/server.json'
    if len(sys.argv) >= 2:
        config_file = sys.argv[1]
    quant.start(config_file=config_file,entrance_func=start)