#coding:utf-8
'''
类方法@classmethod：不是以self作为参数
'''
class Foo(object):
    one = 0

    def __init__(self):
        Foo.one = Foo.one + 1

    @classmethod
    def get_class_attr(cls):
        return cls.one

if __name__ == "__main__":
    f1 = Foo()
    print "f1:",Foo.one
    f2 = Foo()
    print "f2:",Foo.one

    print f1.get_class_attr()
    print "f1.one",f1.one
    print Foo.get_class_attr()

    print "*"* 10
    f1.one = 8
    Foo.one = 9
    print f1.one
    print f1.get_class_attr()
    print Foo.get_class_attr()
