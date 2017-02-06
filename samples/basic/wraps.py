#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/10/16 12:07
# @Author  : Hercwey
# @Site    : 
# @File    : wraps.py
# @Software: PyCharm

"""
装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象。
它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。
有了装饰器，就可以抽离出大量与函数功能本身无关的雷同代码并继续重用。

"""
from functools import wraps


def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)

    return decorated


@decorator_name
def func():
    return ("Function is running")

#测试
can_run = True
print(func())
# Output: Function is running
can_run = False
print(func())
# Output: Function will not run