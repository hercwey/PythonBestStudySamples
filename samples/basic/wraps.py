#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/10/16 12:07
# @Author  : Hercwey
# @Site    : 
# @File    : wraps.py
# @Software: PyCharm

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