#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: Hercwey
@license: Apache Licence 
@contact: 29053631@qq.com
@site: 
@software: PyCharm Community Edition
@file: decorator_example.py
@time: 2016/9/26 12:25
"""

"""
tutorial doc: http://python.jobbole.com/82626/
"""

"""
装饰函数和方法

我们先定义两个简单的数学函数，一个用来计算平方和，一个用来计算平方差：
"""

# get square sum
def square_sum(a, b):
    return a ** 2 + b ** 2

# get square diff
def square_diff(a, b):
    return a ** 2 - b ** 2

print(square_sum(3, 4))
print(square_diff(3, 4))

"""
在拥有了基本的数学功能之后，我们可能想为函数增加其它的功能，比如打印输入。我们可以改写函数来实现这一点：
"""
# modify: print input

# get square sum
def square_sum(a, b):
    print("intput:", a, b)
    return a**2 + b**2

# get square diff
def square_diff(a, b):
    print("input", a, b)
    return a**2 - b**2

print(square_sum(3, 4))
print(square_diff(3, 4))

"""
我们“修改了函数的定义”，为函数增加了功能。
现在我们使用“装饰器”来实现上述修改：
"""
print "-----------------------------------------------------------"
def decorator(F):
    def new_F(a, b):
        print("input", a, b)
        return F(a, b)
    return new_F
print "11111"
# get square sum
@decorator
def square_sum(a, b):
    return a**2 + b**2

# get square diff
@decorator
def square_diff(a, b):
    return a**2 - b**2

print(square_sum(3, 4))
print "2222222"
print(square_diff(3, 4))

print "3333333"

"""
含参的装饰器
装饰器的语法允许我们调用decorator时，提供其它参数，比如@decorator(a)。这样，就为装饰器的编写和使用提供了更大的灵活性。
"""
# a new wrapper layer
def pre_str(pre=''):
    # old decorator
    def decorator(F):
        def new_F(a, b):
            print(pre + "input", a, b)
            return F(a, b)
        return new_F
    return decorator

# get square sum
@pre_str('^_^')
def square_sum(a, b):
    return a**2 + b**2

# get square diff
@pre_str('T_T')
def square_diff(a, b):
    return a**2 - b**2

print(square_sum(3, 4)) # 相当于square_sum = pre_str('^_^') (square_sum)
print(square_diff(3, 4))

print "-----------------------------------------------------------"

"""
装饰类
装饰器可以接收一个类，并返回一个类，从而起到加工类的效果。
"""
def decorator(aClass):
    class newClass:
        def __init__(self, age):
            self.total_display = 0
            self.wrapped = aClass(age)
        def display(self):
            self.total_display += 1
            print("total display", self.total_display)
            self.wrapped.display()
    return newClass

@decorator
class Bird:
    def __init__(self, age):
        self.age = age
    def display(self):
        print("My age is",self.age)

eagleLord = Bird(5)
for i in range(3):
    eagleLord.display()

"""
总结

装饰器的核心作用是name binding。这种语法是Python多编程范式的又一个体现。
大部分Python用户都不怎么需要定义装饰器，但有可能会使用装饰器。
鉴于装饰器在Python项目中的广泛使用，了解这一语法是非常有益的。
"""