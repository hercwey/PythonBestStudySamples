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
