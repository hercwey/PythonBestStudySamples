# -*-coding:utf-8-*-
'''
python中的闭包从表现形式上定义（解释）为：如果在一个内部函数里，对在外部作用域（但不是在全局作用域）的变量进行引用，那么内部函数就被认为是闭包(closure)。

闭包(closure)是函数式编程的重要的语法结构。函数式编程是一种编程范式 (而面向过程编程和面向对象编程也都是编程范式)。
在面向过程编程中，我们见到过函数(function)；在面向对象编程中，我们见过对象(object)。
函数和对象的根本目的是以某种逻辑方式组织代码，并提高代码的可重复使用性(reusability)。
闭包也是一种组织代码的结构，它同样提高了代码的可重复使用性。

不同的语言实现闭包的方式不同。Python以函数对象为基础，为闭包这一语法结构提供支持的 (我们在特殊方法与多范式中，已经多次看到Python使用对象来实现一些特殊的语法)。
Python一切皆对象，函数这一语法结构也是一个对象。在函数对象中，我们像使用一个普通对象一样使用函数对象，比如更改函数对象的名字，或者将函数对象作为参数进行传递。
'''

"""
闭包：函数是一个对象，所以可以作为某个函数的返回结果。
"""


def line_conf():
    def line(x):
        return 2 * x + 1

    return line  # 返回一个函数对象


my_line = line_conf()
print(my_line(5))

"""
一个函数和它的环境变量合在一起，就构成了一个闭包(closure)。
在Python中，所谓的闭包是一个包含有环境变量取值的函数对象。
环境变量取值被保存在函数对象的__closure__属性中。比如下面的代码：
"""


def line_conf2():
    b = 15

    def line(x):
        return 2 * x + b

    return line  # 返回一个函数对象


b = 5
my_line = line_conf2()
print(my_line.__closure__)
print(my_line.__closure__[0].cell_contents)
"""
输出：
(<cell at 0x02407B10: int object at 0x01C6A230>,)
15
__closure__里包含了一个元组(tuple)。
这个元组中的每个元素是cell类型的对象。
我们看到第一个cell包含的就是整数15，也就是我们创建闭包时的环境变量b的取值。
"""

"""
下面看一个闭包的实际例子。
一个函数和它的环境变量合在一起，就构成了一个闭包(closure)。在Python中，所谓的闭包是一个包含有环境变量取值的函数对象。环境变量取值被保存在函数对象的__closure__属性中。
这个例子中，函数line与环境变量a,b构 成闭包。
"""

def line_conf3(a, b):
    def line(x):
        return a * x + b
    return line


line1 = line_conf3(1, 1)
line2 = line_conf3(4, 5)
print(line1(5), line2(5))
