#!/usr/bin/env python
# coding=utf-8

'''
迭代器学习
'''

class MyRange(object):
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            self.i += 1
            return self.i
        else:
            raise StopIteration()

if __name__ == "__main__":
    x = MyRange(3)
    print x
    
    print "self.n=",x.n,";","self.i=",x.i

    x.next()
    print "self.n=",x.n,";","self.i=",x.i

    x.next()
    print "self.n=",x.n,";","self.i=",x.i

    x.next()
    print "self.n=",x.n,";","self.i=",x.i

    x.next()
    print "self.n=",x.n,";","self.i=",x.i

    x.next()
    print "self.n=",x.n,";","self.i=",x.i
