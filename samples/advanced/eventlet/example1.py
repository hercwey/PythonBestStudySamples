# -*- coding:utf-8-*-
"""
tutorial doc:
http://blog.csdn.net/zhaoeryi/article/details/38871737
http://eventlet.net/doc/basic_usage.html

协程介绍如下：
    协程和线程比较像，每个协程都有⾃己的私有stack和局部变量
    一个线程内可以有很多个协程
    多个线程可以同时运行。但在一个线程内，同一时间只有一个协程在运行，无须对某些共享变量加锁
    协程之间的执行顺序，完全由程序来控制
    除非自己放弃执行，否则一直执行到结束
    协程是一种概念，非操作系统可见，在多种语言中实现，如go、ruby等。eventlet是Python中实现之一
"""
from greenlet import greenlet


def test1():
    print 12
    gr2.switch()
    print 34

def test2():
    print 56
    gr1.switch()
    print 78

gr1 = greenlet(test1)
gr2 = greenlet(test2)
print "main thread start..."
gr1.switch()
print "main thread exit."

"""
程序解释：
程序很简单，定义两个协程，最后一行g1.switch()跳转到 test1() ，它打印12，然后跳转到 test2() ，打印56，
然后跳转回 test1() ，打印34，然后 test1() 就结束，gr1死掉，回到父greenlet，不会再切换到test2，
所以不会打印78。在上面的例子中main greenlet就是它们的父greenlet。
"""