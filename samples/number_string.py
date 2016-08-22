#! /usr/bin/python
# -*-coding:utf8-*-
a = 2
b = "test"
# c=a+b
# 运行这行程序会出错,提示你字符串和数字不能连接,于是只好用内置函数进行转换
c = str(a) + b
d = "1234"
e = a + int(d)

# 打印多个值
print("c is %s and e is %i" % (c, e))

''' 
知识点:
* 用int和str函数将字符串和数字进行转换
* 打印以#开头,而不是习惯的//
* 打印多个参数的方式     
'''
