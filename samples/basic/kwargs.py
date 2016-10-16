#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/10/15 13:13
# @Author  : Hercwey
# @Site    : 
# @File    : kwargs.py
# @Software: PyCharm

"""
**kwargs 的⽤法
**kwargs 允许你将不定长度的键值对, 作为参数传递给⼀个函数。 如果你想要在⼀个函
数⾥处理带名字的参数, 你应该使⽤**kwargs。

"""


def toDict(**kwargs):
    a = dict(kwargs)
    print a


if __name__ == "__main__":
    toDict(a=2, b=6)
