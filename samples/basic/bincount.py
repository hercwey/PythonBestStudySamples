#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: Hercwey
@license: Apache Licence 
@contact: 29053631@qq.com
@site: 
@software: PyCharm
@file: bincount.py
@time: 2017/2/7 9:46
"""
"""
  17. 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
"""

def getOneCount(num):

    if num > 0:
        count = b_num.count('1')
        print(b_num)
        return count
    elif num < 0:
        b_num = bin(~num)
        count = 8 - b_num.count('1')
        return count
    else:
        return 8


if __name__ == '__main__':
    print(bin(5))
    #print(getOneCount(5))
    #print(getOneCount(-5))
   # print(getOneCount(0))
