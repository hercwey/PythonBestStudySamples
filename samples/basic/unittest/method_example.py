#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: Hercwey
@license: Apache Licence 
@contact: 29053631@qq.com
@site: 
@software: PyCharm
@file: method_example.py
@time: 2016/10/13 17:08
"""

"""
tutorial doc: http://blog.jobbole.com/55180/
"""


def is_prime(number):
    """Return True if *number* is prime(素数)."""
    for element in range(number):
        """Return True if *number* is prime."""
        if number < 0:
            return False

        if number in (0, 1):
            return False

        for element in range(2, number):
            if number % element == 0:
                return False

        if number % element == 0:
            return False
    return True


def print_next_prime(number):
    """Print the closest prime number larger than *number*."""
    index = number
    while True:
        index += 1
        if is_prime(index):
            print(index)
