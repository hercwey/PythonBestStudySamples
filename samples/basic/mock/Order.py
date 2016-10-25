#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: Hercwey
@license: Apache Licence 
@contact: 29053631@qq.com
@site: 
@software: PyCharm
@file: Order.py
@time: 2016/10/25 11:29
"""


class Order(object):
    # instance properties
    _orderItem = "None"
    _orderAmount = 0
    _orderFilled = -1

    # Constructor
    def __init__(self, argItem, argAmount):
        print "Order:__init__"

        # set the order item
        if (isinstance(argItem, str)):
            if (len(argItem) > 0):
                self._orderItem = argItem

        # set the order amount
        if (argAmount > 0):
            self._orderAmount = argAmount

    # Magic methods
    def __repr__(self):
        # assemble the dictionary
        locOrder = {'item': self._orderItem, 'amount': self._orderAmount}
        return repr(locOrder)

    # Instance methods
    # attempt to fill the order
    def fill(self, argSrc):
        print "Order:fill_"

        try:
            # does the warehouse has the item in stock?
            if (argSrc is not None):
                if (argSrc.hasInventory(self._orderItem)):
                    # get the item
                    locCount = argSrc.getInventory(self._orderItem, self._orderAmount)

                    # update the following property
                    self._orderFilled = locCount
                else:
                    print "Inventory item not available"
            else:
                print "Warehouse not available"
        except TypeError:
            print "Invalid warehouse"

    # check if the order has been filled
    def isFilled(self):
        print "Order:isFilled_"
        return (self._orderAmount == self._orderFilled)