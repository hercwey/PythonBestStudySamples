#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: Hercwey
@license: Apache Licence 
@contact: 29053631@qq.com
@site: 
@software: PyCharm
@file: map_reduce.py
@time: 2017/2/6 11:51
"""
"""
Tutorial: http://www.pythoner.com/46.html
1.map()
格式：map( func, seq1[, seq2...] )
Python函数式编程中的map()函数是将func作用于seq中的每一个元素，并用一个 "列表" 给出返回值。如果func为None，作用同zip()。
"""

# 使用map
print map(lambda x: x%3, range(6)) # [0, 1, 2, 0, 1, 2]

# 使用列表解析
print [x%3 for x in range(6)]  # [0, 1, 2, 0, 1, 2]

# python 函数式编程之map使用（多个seq）
print map(lambda x, y: x * y, [1,2,3],[4,5,6]) # [4, 10, 18]

# Python 函数式编程之map使用（多个seq）
print map(lambda x, y: (x * y, x + y), [1,2,3],[4,5,6])  # [(4, 5), (10, 7), (18, 9)]

# Python函数式编程之map使用（func 为None）
print map(None, [1,2,3],[4,5,6])  # [(1, 4), (2, 5), (3, 6)]
print zip( [1, 2, 3], [4, 5, 6] )  # [(1, 4), (2, 5), (3, 6)]


"""
2.reduce()
格式：reduce( func, seq[, init] )
reduce函数即为化简，它是这样一个过程：每次迭代，将上一次的迭代结果（第一次时为init的元素，如没有init则为seq的第一个元素）
与下一个元素一同执行一个二元的func函数。在reduce函数中，init是可选的，如果使用，则作为第一次迭代的第一个元素使用。
简单来说，可以用这样一个形象化的式子来说明：
reduce( func, [1, 2,3] ) = func( func(1, 2), 3)
"""

"""
举个例子来说，阶乘是一个常见的数学方法，Python中并没有给出一个阶乘的内建函数，我们可以使用reduce实现一个阶乘的代码。
"""
# Python 函数式编程之Reduce使用
n = 5
print reduce(lambda x, y: x * y, range(1, n + 1)) #120

m = 2
n = 5
print reduce(lambda x, y: x * y, range(1, n + 1), m) #240