#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/10/16 13:00
# @Author  : Hercwey
# @Site    : 
# @File    : wraps_parameters.py
# @Software: PyCharm

from functools import wraps


def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile，并写⼊内容
            with open(logfile, 'a') as opened_file:
                # 现在将⽇志打到指定的logfile
                opened_file.write(log_string + '\n')

        return wrapped_function

    return logging_decorator


@logit()
def myfunc1():
    pass


myfunc1()


# Output: myfunc1 was called
# 现在⼀个叫做 out.log 的⽂件出现了，⾥⾯的内容就是上⾯的字符串
@logit(logfile='func2.log')
def myfunc2():
    pass


myfunc2()
# Output: myfunc2 was called
# 现在⼀个叫做 func2.log 的⽂件出现了，⾥⾯的内容就是上⾯的字符串
