#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: Hercwey
@license: Apache Licence 
@contact: 29053631@qq.com
@site: 
@software: PyCharm
@file: lambda.py
@time: 2016/10/18 17:45
"""
"""
lambda表达式是⼀⾏函数。
它们在其他语⾔中也被称为匿名函数。如果你不想在程序中对⼀个函数使⽤两次，你也许
会想⽤lambda表达式，它们和普通的函数完全⼀样。
原型
lambda 参数:操作(参数)
"""
add = lambda x, y: x+y
print(add(1,2))

#列表排序
a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key=lambda x: x[1])
print(a)