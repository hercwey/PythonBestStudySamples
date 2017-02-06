#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: Hercwey
@license: Apache Licence 
@contact: 29053631@qq.com
@site: 
@software: PyCharm
@file: exception2.py
@time: 2017/2/6 11:22
"""

# coding=utf-8

# 自定义异常
class HappyException(Exception):
    pass

# 引发和捕获异常
try:
    raise HappyException
except:
    print("HappyException")

try:
    raise HappyException()
except:
    print("HappyException")

# 捕获多种异常
try:
    raise HappyException
except (HappyException, TypeError):
    print("HappyException")

# 重新引发异常
try:
    try:
        raise HappyException
    except (HappyException, TypeError):
        raise
except:
    print("HappyException")

#访问异常实例
try:
    raise HappyException("都是我的错")
except (HappyException, TypeError), e:
    print(e)

#按类型捕获
try:
    raise HappyException
except HappyException:
    print("HappyException")
except TypeError:
    print("TypeError")

#全面捕获
try:
    raise HappyException
except:
    print("HappyException")

#没有异常的else
try:
    pass
except:
    print("HappyException")
else:
    print("没有异常")

#总会执行的final
try:
    pass
except:
    print("HappyException")
else:
    print("没有异常")
finally:
    print("总会执行")