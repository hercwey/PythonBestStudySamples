#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: Hercwey
@license: Apache Licence 
@contact: 29053631@qq.com
@site: 
@software: PyCharm
@file: deque.py
@time: 2016/10/18 16:02
"""
"""
deque提供了一个双端队列，你可以从头/尾两端添加或删除元素。
"""
from collections import deque

# 它的用法就像python 的list：
d = deque()
d.append('1')
d.append('2')
d.append('3')

# 你可以从两端取出数据：
d = deque(range(5))
print(len(d))
d.popleft()
d.pop()


print (len(d))
