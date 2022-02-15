# -- coding: utf-8 --
# cython: language_level=3
'''
@author:rushi
@version:1.0.0
@time:2022/1/3 21:54
'''
"""
Market Server.

Market Server will get market data from Exchange via Websocket or REST as soon as possible, then packet market data into
MarketEvent and publish into EventCenter.

Date:   2021/08/01
"""

import sys
import signal
from aioquant import const
from aioquant import quant
from aioquant.configure import config
from aioquant.utils import logger
# 防止server closed
import nest_asyncio
nest_asyncio.apply()


def initialize():
    """Initialize Server."""

    if sys.platform.find('win') == -1:
        for s in [signal.SIGHUP, signal.SIGINT, signal.SIGABRT, signal.SIGTERM]:
            signal.signal(s,signal_hander)
    else:
        for s in [signal.SIGINT, signal.SIGABRT, signal.SIGTERM]:
            signal.signal(s,signal_hander)

    for platform in config.markets:
        tmp_platform = platform
        # 合约 ----- rushi 2022-02-12 15:00 start
        # if platform == const.BINANCE_SWAP:
        if platform.find(const.BINANCE_SWAP) != -1:
            tmp_platform = const.BINANCE_SWAP
            from markets.binance_swap_2021 import BinanceSwapMarket as Market
            # pass
        # elif platform == const.GATE_SWAP:
        #     from markets.gate_usdt_swap_2021 import GateMarket as Market
        # elif platform == const.OKEX_FUTURE:
        #     from markets.okex_future_2021 import OKExFutureMarket as Market
        # elif platform == const.BITMEX:
        #     from markets.bitmex_2021 import BitmexMarket as Market
        # 合约 ----- rushi 2022-02-12 15:00 end
        # 现货 ----- rushi 2022-02-12 15:00 start
        elif platform.find(const.BINANCE) != -1:
            tmp_platform = const.BINANCE
            from markets.binance import Binance as Market
            # pass
        # 现货 ----- rushi 2022-02-12 15:00 start
        else:
            logger.error("market-main.py ==> platform error! platform:", platform)
            continue
        cc = config.markets[platform]
        # cc["platform"] = platform
        cc["platform"] = tmp_platform
        Market(**cc)
    logger.info('行情服务器启动...', caller=initialize)

def signal_hander(self, signum=None, frame=None):
    logger.info('行情服务器退出了...', caller=signal_hander)
    quant.stop()

if __name__ == "__main__":
    config_file = 'config/market.json'
    if len(sys.argv) >= 2:
        config_file = sys.argv[1]
    quant.start(config_file, initialize)
