#!/usr/bin/env python
#coding:utf-8

"""
建立一个类，名字是Person,有关于人的基本信息
再建立一个程序员的类，继承Person，增加有关程序员的个性化信息
"""


class Person(object):
    def __init__(self, name):
        self.name = name
        
    def get_sleeptime(self):
        return 11

class Programmer(Person):
    def __init__(self, lang,name):
        super(Programmer, self).__init__(name)
        self.lang = lang
        
    def get_sleeptime(self):
        return 1
        
if __name__ == "__main__":
    p = Programmer("laoqi", "python")
    print p.lang
    print p.get_sleeptime()
