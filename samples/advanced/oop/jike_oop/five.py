# coding=utf-8
'''
多继承之 继承顺序：广度优先
'''
class K1(object):
    def foo(self):
        print "K1-foo"

class K2(object):
    def foo(self):
        print "K2-foo"
    def bar(self):
        print "K2-bar"

class J1(K1, K2):
    pass

class J2(K1, K2):
    def bar(self):
        print "J2-bar"

class C(J1, J2):
    pass

if __name__ == "__main__":
    print C.__mro__
    m = C()
    m.foo()
    m.bar()

#(<class '__main__.C'>, <class '__main__.J1'>, <class '__main__.J2'>,
#    <class '__main__.K1'>, <class '__main__.K2'>, <type 'object'>)
#K1-foo
#J2-bar
