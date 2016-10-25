#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: Hercwey
@license: Apache Licence 
@contact: 29053631@qq.com
@site: 
@software: PyCharm
@file: unittest_example.py
@time: 2016/10/25 13:58
"""
"""
tutorial doc: http://docs.python-guide.org/en/latest/writing/tests/

"""
import unittest


def fun(x):
    return x + 1


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)
