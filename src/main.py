# -- coding: utf-8 --
# cython: language_level=3
'''
@author:rushi
@version:1.0.0
@time:2021/12/30 10:01
python src/main.py 配置 实盘ID 策略标识
'''
import sys
from aioquant import quant

def start():
    if len(sys.argv) >= 6:
        robots_id = sys.argv[2]
        sign = sys.argv[3]
        username = sys.argv[4]
        password = sys.argv[5]
        if robots_id:
            if sign == 'grid':
                from strategy.grid import Grid
                Grid(robots_id,username,password)
        if sign == 'xianhuo':
            from strategy.xianhuo import Xianhuo
            Xianhuo(robots_id, username, password)

if __name__ == '__main__':
    config_file = 'config/main.json'
    if len(sys.argv) >= 2:
        config_file = sys.argv[1]
    quant.start(config_file=config_file,entrance_func=start)