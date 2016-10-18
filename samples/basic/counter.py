#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: Hercwey
@license: Apache Licence 
@contact: 29053631@qq.com
@site: 
@software: PyCharm
@file: counter.py
@time: 2016/10/18 13:37
"""
"""
Counter 是一个计数器，它可以帮助我们针对某项数据进行计数。比如它可以用来计算每个人喜欢多少种颜色：
"""

from collections import Counter

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favs = Counter(name for name, colour in colours)
print(favs)

#统一一个文件
with open('deep_copy.py','rb') as f:
    line_count = Counter(f)
print (line_count)
