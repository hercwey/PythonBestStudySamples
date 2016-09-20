# -*-coding:utf-8-*-

'''
特殊的类属性：
Class.__name__ : 显示类的名字
Class.__doc__ ： 显示文档字符串
Class.__bases__ ：显示类的所有父类的构成元素
Class.__dict__ ： 显示类的所有属性
Class.__module__ ： 显示类所在的模块
Class.__class__ ： 显示类的类型
-----------------------
特殊的实例属性：
l.__class__ :
l.__dict__ :
-----------------------
特殊的方法：
__init__() : 初始化/构造器方法
__new__() : 构造器方法, 在__init__()方法执行之前执行的, new方法可以return语句，而init方法不能有。
__del__() : 解构器，是实例释放前提供特殊功能的方法。

===========================================
用特殊方法定制类
类和对象类型

------------------------
简单定制

------------------------
稍复杂定制

------------------------

===========================================
迭代器和生成器



'''


class F(object):
    def __init__(self):
        self.lang = 'python'

    def get_lang(self):
        print self.lang


class F(object):
    """This is my class"""

    def __init__(self):
        self.lang = "python"

    def get_lang(self):
        print self.lang


print(F.__name__)
print(F.__doc__)
print(F.__bases__)


class C(F):
    pass


print(C.__bases__)


class A(object):
    def __new__(cls):
        print"A.__new__ called"
        return super(A, cls).__new__(cls)

    def __init__(self):
        print "A.__init__called"


A()


class RoundFloat(float):
    def __new__(cls, val):
        return super(RoundFloat, cls).__new__(cls, round(val, 2))

print RoundFloat(3.1415)
