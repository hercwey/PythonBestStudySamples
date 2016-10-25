#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: Hercwey
@license: Apache Licence 
@contact: 29053631@qq.com
@site: 
@software: PyCharm
@file: listing_eight.py
@time: 2016/10/25 11:20
"""
"""
http://www.oschina.net/translate/unit-testing-with-the-python-mock-class
mock 断言
"""
from mock import Mock


# The mock object
class Foo(object):
    # instance properties
    _fooValue = 123

    def callFoo(self):
        pass

    def doFoo(self, argValue):
        pass


# create the mock object
mockFoo = Mock(spec=Foo)
print mockFoo
# returns <Mock spec='Foo' id='507120'>

mockFoo.doFoo("narf")
mockFoo.doFoo.assert_called_with("narf")
# assertion passes

mockFoo.doFoo("zort")
mockFoo.doFoo.assert_called_with("narf")
# AssertionError: Expected call: doFoo('narf')
# Actual call: doFoo('zort')