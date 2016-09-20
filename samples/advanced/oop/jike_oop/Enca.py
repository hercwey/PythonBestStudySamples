#coding:utf-8
'''
封装，指类变量与方法可见性， 私有化方法以双下划线"__"开头
'''
class ProtectMe(object):
    def __init__(self):
        self.me = "qiwsir"
        self.__name = "kivi"

    # 下划线表示私有方法
    def __python(self):
        print "I love Python."

    def code(self):
        print 'which language do you like?'
        self.__python()

    @property
    def name(self):
        return self.__name

if __name__ == "__main__":
    p = ProtectMe()
    print p.name
    
    print p.me
    #print p.__name
    p.code()
    p.__python()
