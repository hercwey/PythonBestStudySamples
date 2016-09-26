#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: Hercwey
@license: Apache Licence 
@contact: 29053631@qq.com
@site: 
@software: PyCharm Community Edition
@file: @example.py
@time: 2016/9/26 11:44
"""
"""
python 2.4以后，增加了@符号修饰函数对函数进行修饰，python3.0/2.6又增加了对类的修饰。
@修饰符挺像是处理函数或类之前进行预处理。
语法示例：
@dec1
@dec2
def test(arg):
    pass
其效果类似于
dec1(dec2(test(arg)))
修饰函数还可以带参数。
@dec1(arg1,arg2)
def test(testarg)
效果类似于
dec1(arg1,arg2)(test(arg))

用法示例: 参数类型和返回值类型检查
对于python这样的动态语言，不像C++这样的一开始就有严格静态的类型定义。
但是，在某些情况下，就需要这样的类型检查，那么可以采用＠修饰的方式。下面的示例就是检查输入参数类型和返回值类型的例子。
"""


def accepts(*types):
    def check_accepts(f):
        assert len(types) == f.func_code.co_argcount

        def new_f(*args, **kwds):
            for (a, t) in zip(args, types):
                assert isinstance(a, t), "arg %r does not match %s " % (a, t)
            return f(*args, **kwds)

        new_f.func_name = f.func_name
        return new_f

    return check_accepts


def returns(rtype):
    def check_returns(f):
        def new_f(*args, **kwds):
            result = f(*args, **kwds)
            assert isinstance(result, rtype), "return value %r does not match %s " % (result, rtype)
            return result

        new_f.func_name = f.func_name
        return new_f

    return check_returns


@accepts(int, (int, float))
@returns((int, float))
def func(arg1, arg2):
    return arg1 * arg2


if __name__ == '__main__ ':
    a = func(3, 2.5 )
