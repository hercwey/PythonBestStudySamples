#coding:utf-8

class Person(object):
    def eye(self):
        print "two eyes"

    def breast(self, n):
        print "The breast is:", n

class Girl(object):
    def __init__(self, age):
        self.age = age

    def color(self):
        print "The girl is white."

#多继承
class BeaGirl(Person, Girl):
    pass

if __name__ == "__main__":
    kong = BeaGirl(28)
    kong.eye()
    kong.breast(90)
    kong.color()
    print kong.age

#two eyes
#The breast is: 90
#The girl is white.
#28
