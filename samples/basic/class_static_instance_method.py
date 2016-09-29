#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: Hercwey
@license: Apache Licence 
@contact: 29053631@qq.com
@site: 
@software: PyCharm Community Edition
@file: class_static_instance_method.py
@time: 2016/9/29 13:46
"""

"""
类方法，静态方法，类实例方法区别
"""


class A(object):
    def foo(self, x):
        """类实例方法"""
        print "executing foo(%s, %s)" % (self, x)

    @classmethod  # 声明类方法
    def class_foo(cls, x):
        """类方法"""
        print "executing class_foo(%s, %s)" % (cls, x)

    @staticmethod  # 声明静态方法
    def static_foo(x):
        """静态方法"""
        print "executing static_foo(%s)" % x

#调用方法
a = A()
a.foo(1)
#A.foo(1) # 不能执行
a.class_foo(1)
A.class_foo(1)
a.static_foo(1)
A.static_foo(1)

"""
总结：
区别：类方法和静态方法都可以被类和类的实例调用，类实例方法仅可以被类实例调用。
类方法的隐含调用参数是类，而类实例方法的隐含调用参数是类的实例，静态方法没有隐含调用参数。
按照惯例，类方法的第一个形参被命名为cls.任何时候定义类方法都不是必须的（类方法能实现的功能都可以通过定义一个普通函数来实现，
只要这个函数接受一个类对象作为参数就可以了）
python中实现静态方法和类方法都是依赖于python的修饰器来实现的。对象方法有self参数，类方法有cls参数，静态方法是不需要这些附加参数的。
"""
