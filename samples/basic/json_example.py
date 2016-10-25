#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: Hercwey
@license: Apache Licence 
@contact: 29053631@qq.com
@site: 
@software: PyCharm
@file: json_example.py
@time: 2016/10/25 14:39
"""

"""
tutorial: http://docs.python-guide.org/en/latest/scenarios/json/#parsing-json
解析json
"""

import json

json_string = '{"first_name": "Guido", "last_name":"Rossum"}'

#转换为一个dict
parse_json = json.loads(json_string)

print(parse_json)
print(parse_json['first_name'])

#转换dict为JSON
d = {
    'first_name': 'Guido',
    'second_name': 'Rossum',
    'titles': ['BDFL', 'Developer'],
}
print(json.dumps(d))


