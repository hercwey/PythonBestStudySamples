#coding:utf-8

'''
绑定方法与非绑定方法
'''
class Foo(object):
    one = 0

    def __init__(self):
        Foo.one = Foo.one + 1

def get_class_attr(cls):
    return cls.one

if __name__ == "__main__":
    f1 = Foo()
    print "f1:",Foo.one
    f2 = Foo()
    print "f2:",Foo.one

    print get_class_attr(Foo)
