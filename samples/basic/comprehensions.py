#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: Hercwey
@license: Apache Licence 
@contact: 29053631@qq.com
@site: 
@software: PyCharm
@file: comprehensions.py
@time: 2016/10/18 16:43
"""
"""
各种推导式(comprehensions)
推导式（又称解析式）是Python的⼀种独有特性，如果我被迫离开了它，我会⾮常想念。

推导式是可以从⼀个数据序列构建另⼀个新的数据序列的结构体。

共有三种推导，在
Python2和3中都有⽀持：
列表(list)推导式
字典(dict)推导式
集合(set)推导式
我们将⼀⼀进⾏讨论。⼀旦你知道了使⽤列表推导式的诀窍，你就能轻易使⽤任意⼀种推
导式了。
"""

"""
列表推导式（list comprehensions）
列表推导式（又称列表解析式）提供了⼀种简明扼要的⽅法来创建列表。
它的结构是在⼀个中括号⾥包含⼀个表达式，然后是⼀个for语句，然后是0个或多个for
或者if语句。那个表达式可以是任意的，意思是你可以在列表中放⼊任意类型的对象。返
回结果将是⼀个新的列表，在这个以if和for语句为上下⽂的表达式运⾏完成之后产⽣。
规范
variable = [out_exp for out_exp in input_list if out_exp == 2]
"""

multiples = [i for i in range(30) if i % 3 is 0]
print(multiples)

"""
这将对快速⽣成列表⾮常有⽤。
有些⼈甚⾄更喜欢使⽤它⽽不是filter函数。
列表推导式在有些情况下超赞，特别是当你需要使⽤for循环来⽣成⼀个新列表。举个例
⼦，你通常会这样做：
"""
squared = []
for x in range(10):
    squared.append(x**2)
# 你可以使用列表推导式来简化它，就像这样：
squared = [x**2 for x in range(10)]
print(squared)

"""
字典推导式（dict comprehensions）
字典推导和列表推导的使⽤⽅法是类似的。这⾥有个我最近发现的例⼦：
"""

mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}

mydict = {v: k for k, v in mcase.items()}
print(mydict)

"""
集合推导式（set comprehensions）
它们跟列表推导式也是类似的。 唯⼀的区别在于它们使⽤⼤括号{}。 举个例⼦：
"""
squared = {x**2 for x in [1, 1, 2]}
print(squared)
print(type(squared))
# Output: {1, 4}
