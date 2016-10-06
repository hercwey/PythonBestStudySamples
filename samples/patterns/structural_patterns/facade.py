#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/10/6 12:21
# @Author  : Hercwey
# @Site    : 
# @File    : facade.py
# @Software: PyCharm

# !/usr/bin/env python
# -*- coding: utf-8 -*-

#https://github.com/faif/python-patterns/blob/master/facade.py
# 门面/外观模式：http://www.cnblogs.com/zhenyulu/articles/55992.html
import time

SLEEP = 0.1


# Complex Parts
class TC1:
    def run(self):
        print("###### In Test 1 ######")
        time.sleep(SLEEP)
        print("Setting up")
        time.sleep(SLEEP)
        print("Running test")
        time.sleep(SLEEP)
        print("Tearing down")
        time.sleep(SLEEP)
        print("Test Finished\n")


class TC2:
    def run(self):
        print("###### In Test 2 ######")
        time.sleep(SLEEP)
        print("Setting up")
        time.sleep(SLEEP)
        print("Running test")
        time.sleep(SLEEP)
        print("Tearing down")
        time.sleep(SLEEP)
        print("Test Finished\n")


class TC3:
    def run(self):
        print("###### In Test 3 ######")
        time.sleep(SLEEP)
        print("Setting up")
        time.sleep(SLEEP)
        print("Running test")
        time.sleep(SLEEP)
        print("Tearing down")
        time.sleep(SLEEP)
        print("Test Finished\n")


# Facade
class TestRunner:
    def __init__(self):
        self.tc1 = TC1()
        self.tc2 = TC2()
        self.tc3 = TC3()
        self.tests = [self.tc1, self.tc2, self.tc3]

    def runAll(self): # 组合调用后端对象方法
        [i.run() for i in self.tests]


# Client
if __name__ == '__main__':
    testrunner = TestRunner()
    testrunner.runAll() # 在门面的地方来进行组合调用，而不是直接调用门面后面的对象方法

    ### OUTPUT ###
    # ###### In Test 1 ######
    # Setting up
    # Running test
    # Tearing down
    # Test Finished
    #
    # ###### In Test 2 ######
    # Setting up
    # Running test
    # Tearing down
    # Test Finished
    #
    # ###### In Test 3 ######
    # Setting up
    # Running test
    # Tearing down
    # Test Finished
    #

"""
一句话解释：外部与一个子系统的通信必须通过一个统一的门面(Facade)对象进行，这就是门面模式。
就如同医院的接待员一样，门面模式的门面类将客户端与子系统的内部复杂性分隔开，使得客户端只需要与门面对象打交道，
而不需要与子系统内部的很多对象打交道。

适用场景：
为一个复杂子系统提供一个简单接口
提高子系统的独立性
在层次化结构中，可以使用Facade模式定义系统中每一层的入口。

"""