#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: Hercwey
@license: Apache Licence 
@contact: 29053631@qq.com
@site: 
@software: PyCharm
@file: data_serialization.py
@time: 2016/10/25 15:36
"""
"""
数据序列化：http://docs.python-guide.org/en/latest/scenarios/serialization/#what-is-data-serialization
序列化 的概念很简单。内存里面有一个数据结构，你希望将它保存下来，重用，或者发送给其他人。你会怎么做？嗯, 这取决于你想要怎么保存，怎么重用，发送给谁。
native的数据序列化的模块是pickle。
什么东西能用pickle 模块存储?

所有Python支持的 原生类型 : 布尔, 整数, 浮点数, 复数, 字符串, bytes (字节串)对象, 字节数组, 以及 None .
由任何原生类型组成的列表，元组，字典和集合。
由任何原生类型组成的列表，元组，字典和集合组成的列表，元组，字典和集合(可以一直嵌套下去，直至Python支持的最大递归层数 ).
函数，类，和类的实例(带警告)。
"""

import pickle

#实例dict
grades = { 'Alice': 89, 'Bob': 72, 'Charles': 87 }

#使用dumps方法将对象转换为序列化字符串
serial_grades = pickle.dumps(grades)
print(serial_grades)

#使用loads方法反序列化为一个对象
received_grades = pickle.loads(serial_grades)
print(received_grades)


