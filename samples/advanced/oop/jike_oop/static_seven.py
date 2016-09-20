# -*-coding:utf-8-*-
'''
静态方法
'''
T = 1

def check_t():
    T = 3
    return T 

class Foo(object):
    def __init__(self,name):
        self.name = name

    def get_name(self):
        if check_t():        # call a function out of the class
            return self.name
        else:
            return "no person"

if __name__ == "__main__":

    f = Foo("canglaoshi")
    name = f.get_name()
    print name
