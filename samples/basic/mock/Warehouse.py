#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: Hercwey
@license: Apache Licence 
@contact: 29053631@qq.com
@site: 
@software: PyCharm
@file: Warehouse.py
@time: 2016/10/25 11:30
"""


class Warehouse(object):
    # private properties
    _houseName = None
    _houseList = None

    # accessors
    def warehouseName(self):
        return (self._houseName)

    def inventory(self):
        return (self._houseList)

    # -- INVENTORY ACTIONS
    # set up the warehouse
    def setup(self, argName, argList):
        pass  # check for an inventory item

    def hasInventory(self, argItem):
        pass

        # retrieve an inventory item

    def getInventory(self, argItem, argCount):
        pass

    # add an inventory item
    def addInventory(self, argItem, argCount):
        pass
