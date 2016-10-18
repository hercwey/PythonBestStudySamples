#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: Hercwey
@license: Apache Licence 
@contact: 29053631@qq.com
@site: 
@software: PyCharm
@file: introspection.py
@time: 2016/10/18 16:17
"""
"""
⾃省(introspection)，在计算机编程领域⾥，是指在运⾏时来判断⼀个对象的类型的能⼒。
它是Python的强项之⼀。Python中所有⼀切都是⼀个对象，⽽且我们可以仔细勘察那些对
象。Python还包含了许多内置函数和模块来帮助我们。
"""

"""
dir
它是⽤于⾃省的最重要的函数之⼀。它返回⼀个列表，列出了⼀个对象所拥有的属性和⽅法。
"""
my_list = list(range(5))
dir(my_list)

"""
type和id
type函数返回⼀个对象的类型。
"""

print(type(''))
# Output: <type 'str'>
print(type([]))
# Output: <type 'list'>
print(type({}))
# Output: <type 'dict'>
print(type(dict))
# Output: <type 'type'>
print(type(3))
# Output: <type 'int'>
# id()函数返回任意不同种类对象的唯⼀ID，举个例⼦：
name = "Yasoob"
print(id(name))

"""
inspect模块
inspect模块也提供了许多有⽤的函数，来获取活跃对象的信息。⽐⽅说，你可以查看⼀
个对象的成员，只需运⾏：
"""
import inspect
print (inspect.getmembers(dict))