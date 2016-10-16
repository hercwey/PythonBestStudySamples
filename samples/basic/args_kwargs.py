#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/10/15 13:28
# @Author  : Hercwey
# @Site    : 
# @File    : args_kwargs.py
# @Software: PyCharm

import pdb
def test_args_kwargs(arg1, arg2, arg3):
    pdb.set_trace()
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


# ⾸先使⽤ *args
args = ("two", 3, 5)
print test_args_kwargs(*args)

# 现在使⽤ **kwargs:
kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
print test_args_kwargs(**kwargs)

print test_args_kwargs(arg3=3, arg2="two", arg1=5)

"""
pdb命令列表：
c: 继续执⾏
w: 显⽰当前正在执⾏的代码⾏的上下⽂信息
a: 打印当前函数的参数列表
s: 执⾏当前代码⾏，并停在第⼀个能停的地⽅（相当于单步进⼊）
n: 继续执⾏到当前函数的下⼀⾏，或者当前⾏直接返回（单步跳过）
"""
