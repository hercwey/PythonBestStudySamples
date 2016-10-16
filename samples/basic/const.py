#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/10/16 18:28
# @Author  : Hercwey
# @Site    : 
# @File    : const.py
# @Software: PyCharm
"""
python 常量类的写法
"""


#coding:utf-8
class _const:
    class ConstError( TypeError ): pass
    class ConstCaseError( ConstError ): pass

    def __setattr__( self, name, value ):
        if name in self.__dict__:
            raise self.ConstError( "can't change const %s" % name )
        if not name.isupper():
            raise self.ConstCaseError( 'const name "%s" is not all uppercase' % name )
        self.__dict__[name] = value

const = _const()
const.PI = 3.1415926
const.AUTHOR = "Hercwey"
