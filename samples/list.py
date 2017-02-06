#! /usr/bin/python
# -*-coding:utf8-*-

# 定义列表
word = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# 通过索引访问列表里的元素
a = word[2]
print("a is %s" % a)
b = word[1:3]
print("b is: ")
print(b)  # index 1 and 2 elements of word. 
c = word[:2]
print("c is: ")
print(c)  # index 0 and 1 elements of word. 
d = word[0:]
print("d is: ")
print(d)  # All elements of word.

# 合并列表
e = word[:2] + word[2:]
print("e is: ")
print(e)  #  All elements of word. 
f = word[-1]
print("f is: ")
print(f)  #  The last elements of word. 
g = word[-4:-2]
print("g is: ")
print(g)  #  index 3 and 4 elements of word. 
h = word[-2:]
print("h is: ")
print(h)  #  The last two elements. 
i = word[:-2]
print("i is: ")
print(i)  #  Everything except the last two characters 
l = len(word)
print("Length of word is: " + str(l))
print("Adds new element")
word.append('h')
print(word)
# 删除元素
del word[0]
print (word)
del word[1:3]
print(word)
print('中文')

''' 
知识点:
* 列表长度是动态的,可任意添加删除元素. 
* 用索引可以很方便访问元素,甚至返回一个子列表     
* 更多方法请参考Python的文档
'''
