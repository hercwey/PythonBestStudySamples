#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/10/16 18:29
# @Author  : Hercwey
# @Site    : 
# @File    : constant_use.py
# @Software: PyCharm
from const import const
print const.PI
print const.AUTHOR
const.PI = 3.14 # 抛出异常，常量不能修改