# -- coding: utf-8 --
# cython: language_level=3
'''
@author:rushi
@version:1.0.0
@time:2022/1/10 17:18
'''
import time

# 返回秒级别时间戳
def Unix():
    t = time.time()
    return int(t)

def get_cur_timestamp_ms():
    """Get current timestamp(millisecond)."""
    t = time.time()
    ts = int(round(t * 1000))
    return ts

# 当天时间str
def getDayTime():
    # stmp = time.localtime()
    return time.strftime('%Y-%m-%d')

# 格式化时间
def D(secs = None):
    secs = secs or Unix()
    fmt = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(secs))
    return fmt

# 格式化一个浮点数
def N(Num,Precision):
    Num = float(Num)
    Precision = int(Precision)
    TmpPrecision = 10**Precision
    Num = int(float(Num * TmpPrecision)) / TmpPrecision
    return Num

def get_binance_swap_amount(currencys,amount):
    """
    取币安合约数量精度
    rushi 2022-01-12 15:00
    :param currencys:
    :param amount:
    :return:
    """
    # if currencys and amount:
    #     currencys_dict = {
    #         'DOGEUSDT':0
    #     }
    #     if currencys in currencys_dict:
    #         amount = N(amount,currencys_dict.get(currencys))
    return amount

def get_binance_swap_price(currencys,price):
    """
    取币安合约价格精度
    rushi 2022-01-12 15:00
    :param currencys:
    :param price:
    :return:
    """
    # if currencys and price:
    #     currencys_dict = {
    #         'DOGEUSDT':5
    #     }
    #     if currencys in currencys_dict:
    #         price = N(price,currencys_dict.get(currencys))
    return price

def _Cross(list1,list2):
    """
    _Cross(Arr1, Arr2)，返回数组arr1与arr2的交叉周期数。正数为上穿周期，负数表示下穿的周期，0指当前价格一样。参数值：数值类型数组。
    https://www.fmz.com/bbs-topic/1140
    :param list1:
    :param list2:
    :return:
    """
    if len(list1) != len(list2):
        # return 'list length not equal'
        # 这里应该抛出错误
        return 0
    n = 0
    # 遍历list1，遍历顺序为从最后一个元素向前遍历
    tmp_len = len(list1)
    for i in range(tmp_len):
        tmp_i = tmp_len - i - 1
        """
            if (typeof(arr1[i]) !== 'number' || typeof(arr2[i]) !== 'number') { // 当arr1或者arr2任何一个数组为非数值类型（即无效指标）时，跳出遍历循环
                break;                                  // 跳出循环
            }
        """
        # print(type(list1[tmp_i]),type(list2[tmp_i]))
        if int(list1[tmp_i]) < int(list2[tmp_i]):
            if n > 0:
                break
            n = n - 1
        elif int(list1[tmp_i]) > int(list2[tmp_i]):
            if n < 0:
                break
            n = n + 1
        else:
            break
    return n

