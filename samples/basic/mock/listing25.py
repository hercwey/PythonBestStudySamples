#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: Hercwey
@license: Apache Licence 
@contact: 29053631@qq.com
@site: 
@software: PyCharm
@file: listing25.py
@time: 2016/10/25 11:25
"""
"""
Listing Twenty-five是测试用例本身，orderTest类。他有一个属性fooSource是Order类所需的mock对象。
setUp()方法识别执行的测试例程，然后创建和配置mock对象。tearDown()方法向stdout打印一个空行。
"""

import unittest_example

from mock import Mock, call
import Order, Warehouse


class OrderTest(unittest_example.TestCase):
    # declare the test resource
    fooSource = None

    # preparing to test
    def setUp(self):
        """ Setting up for the test """
        print "OrderTest:setUp_:begin"

        # identify the test routine
        testName = self.id().split(".")
        testName = testName[2]
        print testName

        # prepare and configure the test resource
        if (testName == "testA_newOrder"):
            print "OrderTest:setup_:testA_newOrder:RESERVED"
        elif (testName == "testB_nilInventory"):
            self.fooSource = Mock(spec=Warehouse, return_value=None)
        elif (testName == "testC_orderCheck"):
            self.fooSource = Mock(spec=Warehouse)
            self.fooSource.hasInventory.return_value = True
            self.fooSource.getInventory.return_value = 0
        elif (testName == "testD_orderFilled"):
            self.fooSource = Mock(spec=Warehouse)
            self.fooSource.hasInventory.return_value = True
            self.fooSource.getInventory.return_value = 10
        elif (testName == "testE_orderIncomplete"):
            self.fooSource = Mock(spec=Warehouse)
            self.fooSource.hasInventory.return_value = True
            self.fooSource.getInventory.return_value = 5
        else:
            print "UNSUPPORTED TEST ROUTINE"

    # ending the test
    def tearDown(self):
        """Cleaning up after the test"""
        print "OrderTest:tearDown_:begin"
        print ""

    # test: new order
    # objective: creating an order
    def testA_newOrder(self):
        # creating a new order
        testOrder = Order("mushrooms", 10)
        print repr(testOrder)

        # test for a nil object
        self.assertIsNotNone(testOrder, "Order object is a nil.")

        # test for a valid item name
        testName = testOrder._orderItem
        self.assertEqual(testName, "mushrooms", "Invalid item name")

        # test for a valid item amount
        testAmount = testOrder._orderAmount
        self.assertGreater(testAmount, 0, "Invalid item amount")

    # test: nil inventory
    # objective: how the order object handles a nil inventory
    def testB_nilInventory(self):
        """Test routine B"""
        # creating a new order
        testOrder = Order("mushrooms", 10)
        print repr(testOrder)

        # fill the order
        testSource = self.fooSource()
        testOrder.fill(testSource)

        # print the mocked calls
        print self.fooSource.mock_calls

        # check the call history
        testCalls = [call()]
        self.fooSource.assert_has_calls(testCalls)

        # ... continued in the next listing