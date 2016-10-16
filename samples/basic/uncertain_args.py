#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/10/15 12:48
# @Author  : Hercwey
# @Site    : 
# @File    : uncertain_args.py
# @Software: PyCharm
"""
*args 的⽤法
*args 和 **kwargs 主要⽤于函数定义。 你可以将不定数量的参数传递给⼀个函数。
这⾥的不定的意思是：预先并不知道, 函数使⽤者会传递多少个参数给你, 所以在这个场景
下使⽤这两个关键字。 *args 是⽤来发送⼀个⾮键值对的可变数量的参数列表给⼀个函数.

"""


def test(a, *args):
    print "常规参数: %s" % a
    for arg in args:
        print "不确定数量的参数：%s" %  arg


if __name__ == "__main__":
    test("qwe", "a", "b", "c")
