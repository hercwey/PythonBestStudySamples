#!/usr/bin/env python
# -*-coding: utf-8-*-
'''
定制类：浮点数保留两位小数
'''


class RoundFloat(object):
    def __init__(self, val):
        assert isinstance(val, float), "value must be a float."
        self.value = round(val, 2)

    def __str__(self):
        return "{:.2f}".format(self.value)

    __repr__ = __str__

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    r = RoundFloat(4.0)
    print r
    print type(r)
