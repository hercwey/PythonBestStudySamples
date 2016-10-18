#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: Hercwey
@license: Apache Licence 
@contact: 29053631@qq.com
@site: 
@software: PyCharm
@file: defaultdict.py
@time: 2016/10/17 17:20
"""

"""
与dict类型不同，你不需要检查key是否存在，所有我们可以这样做
"""
from collections import defaultdict
import json

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favourite_colours = defaultdict(list)

for name, colour in colours:
    favourite_colours[name].append(colour)

print (favourite_colours)

#转换为json
print(json.dumps(favourite_colours))