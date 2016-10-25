#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: Hercwey
@license: Apache Licence 
@contact: 29053631@qq.com
@site: 
@software: PyCharm
@file: mock_tutorial.py
@time: 2016/10/25 13:52
"""

"""
mock tutorial: http://python-mock-tutorial.readthedocs.io/en/latest/mock.html
"""
from mock import Mock
my_mock = Mock()

my_mock.answer.return_value = 42
my_mock.answer()
