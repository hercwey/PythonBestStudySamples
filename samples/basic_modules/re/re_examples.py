# -*-coding:utf-8-*-
import re

'''
1. Python 中的原始类型字符串
Python编译器用‘\’（反斜杠）来表示字符串常量中的转义字符。
原始类型字符串可以简单的通过在普通字符串的双引号前面加一个字符‘r’来创建。
当一个字符串是原始类型时，Python编译器不会对其尝试做任何的替换。
本质上来讲，你在告诉编译器完全不要去干涉你的字符串。
'''
string = 'This is a\nnormal string'
rawString = r'and this is a\nraw string'
print string
# 这是一个普通字符串
print rawString
# 这是一个原始类型字符串。

'''
2. 使用re.match查找 - 匹配开始
match()方法的工作方式是只有当被搜索字符串的开头匹配模式的时候它才能查找到匹配对象。
举个例子，对字符串‘dog cat dog’调用mathch()方法，查找模式‘dog’将会匹配：
'''

