# -- coding: utf-8 --
# cython: language_level=3
'''
@author:rushi
@version:1.0.0
@time:2022/1/7 17:53
'''
import sys
from aioquant import quant
from aioquant.utils import logger

def main():
    from aioquant.configure import config
    from aioquant.event import EventConfig
    # server_id可通过sdk生成交发送给远端服务器保存下来
    server_id = "f1cb9acc-6fa3-11ec-bc39-18c04dbbb318"
    params = {
        "aa":134
    }
    EventConfig(server_id, params).publish()
    logger.info("update config successfully.")
    quant.stop()

if __name__ == "__main__":
    config_file = 'config/grid.json'
    quant.start(config_file=config_file, entrance_func=main)