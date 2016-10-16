#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/10/15 21:20
# @Author  : Hercwey
# @Site    : 
# @File    : map_filter.py
# @Software: PyCharm

"""
Map
Map会将⼀个函数映射到⼀个输⼊列表的所有元素上。这是它的规范：
规范
map(function_to_apply, list_of_inputs)
⼤多数时候，我们要把列表中所有元素⼀个个地传递给⼀个函数，并收集输出。
"""
# 比方说：
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i ** 2)
print squared

# Map 可以让我们用一种简单而漂亮的方式来实现。
squared = list(map(lambda x: x ** 2, items))
print squared
print(list(map(lambda x: x ** 2, items)))
print(list(map(lambda x: x > 2, items)))
print(map(lambda x: x ** 2, items))
print list("abcd")

"""
Filter
顾名思义，filter能创建⼀个列表，其中每个元素都是对⼀个函数能返回True.
"""
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)
print(filter(lambda x: x < 0, number_list))
