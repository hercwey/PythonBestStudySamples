#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: Hercwey
@license: Apache Licence 
@contact: 29053631@qq.com
@site: 
@software: PyCharm
@file: list2.py
@time: 2017/2/6 23:31
"""


def extend_list(val, list=[]):
    list.append(val)
    return list


list1 = extend_list(10)
print(list1)  # list1 = [10]
list2 = extend_list(123, [])
list3 = extend_list('a')

print(list1)  # list1 = [10, 'a']
print(list2)  # list2 = [123, []]
print(list3)  # list3 = [10, 'a']
