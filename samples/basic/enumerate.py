#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: Hercwey
@license: Apache Licence 
@contact: 29053631@qq.com
@site: 
@software: PyCharm
@file: enumerate.py
@time: 2016/10/18 16:08
"""
"""
枚举Enumerate
枚举(enumerate)是Python内置函数。它的⽤处很难在简单的⼀⾏中说明，但是⼤多数的
新⼈，甚⾄⼀些⾼级程序员都没有意识到它。
它允许我们遍历数据并自动计数
"""

my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 3):
    print(c, value)

