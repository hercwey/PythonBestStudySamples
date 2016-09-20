
class A(object): 

    #def __new__(cls):
    #    print "A.__new__ called"
        #return super(A, cls).__new__(cls)
    #    return 12

    def __init__(self):
        print "A.__init__ called"
        return 12

A()
