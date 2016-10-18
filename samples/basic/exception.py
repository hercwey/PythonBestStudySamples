#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/9/26 23:27
# @Author  : Hercwey
# @Site    : 
# @File    : exception.py
# @Software: PyCharm Community Edition
"""
异常处理是⼀种艺术，⼀旦你掌握，会授予你⽆穷的⼒量。我将要向你展⽰我们能处理异
常的⼀些⽅式。
最基本的术语⾥我们知道了try/except从句。可能触发异常产⽣的代码会放到try语句
块⾥，⽽处理异常的代码会在except语句块⾥实现。这是⼀个简单的例⼦：
"""
try:
    file = open('test.txt', 'rb')
except IOError as e:
    print e
    print ('An IOError occured.{}'.format(e.args[-1]))

"""
处理多个异常
我们可以使⽤三种⽅法来处理多个异常。
第⼀种⽅法需要把所有可能发⽣的异常放到⼀个元组⾥。像这样：
"""
try:
    file = open('test.txt', 'rb')
except EOFError as e:
    print("An EOF error occurred.")
    raise e
except IOError as e:
    print("An error occurred.")
    raise e

"""
finally从句
我们把我们的主程序代码包裹进了try从句。然后我们把⼀些代码包裹进⼀个except从
句，它会在try从句中的代码触发异常时执⾏。
在下⾯的例⼦中，我们还会使⽤第三个从句，那就是finally从句。包裹到finally从
句中的代码不管异常是否触发都将会被执⾏。这可以被⽤来在脚本执⾏之后做清理⼯作。
这⾥是个简单的例⼦：
"""
try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('An IOError occurred. {}'.format(e.args[-1]))
finally:
    print("This would be printed whether or not an exception occurred!")
