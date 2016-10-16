#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/10/16 12:52
# @Author  : Hercwey
# @Site    : 
# @File    : wraps_logging.py
# @Software: PyCharm
"""
除了授权认证，⽇志(Logging)
⽇志是装饰器运⽤的另⼀个亮点。
"""
from  functools import wraps


def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return with_logging


@logit
def addition_func(x):
    """Do some math."""
    return x + x


# 测试

result = addition_func(4)

print  result
