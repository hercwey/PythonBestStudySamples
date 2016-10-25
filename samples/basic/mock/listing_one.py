#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: Hercwey
@license: Apache Licence 
@contact: 29053631@qq.com
@site: 
@software: PyCharm
@file: listing_one.py
@time: 2016/10/25 11:04
"""

"""
构造器的第一个参数是name，它定义了mock对象的唯一标示符。Listing one显示了怎么创建一个标示符为Foo的mock对象mockFoo。
"""

from mock import Mock

# 创建mock对象
mockFoo = Mock(name="Foo")

print mockFoo
#return <Mock name='Foo' id='38585264'>
print repr(mockFoo)
#return <Mock name='Foo' id='38585264'>
