# -*-coding: utf-8-*-
"""
最常被使用的python代码片段
tutorial doc: http://www.programcreek.com/2015/05/most-frequently-used-python-code-fragments-for-java-developers/
"""

"""
过滤列表list
"""
list = ['a12', '32', '  ', 'f34', 'bd', ' ', '4', 'zz']
# 过滤list中的空字符串
l1 = [x for x in list if x.strip() != '']
print l1
# 过滤list中为不是数字的字符串
l2 = [x for x in list if x.isdigit()]
print l2
print "----------------------------------------------------------\n"
"""
按行读取文件
"""
with open("readingfile") as f:
    for line in f:
        print line
print "----------------------------------------------------------\n"

"""
按行写文件
"""
aList = ["line1.........", "line2.........."]
f = open("writingfile", 'w')
for e in aList:
    f.write(e + "\n")
f.close()
print "----------------------------------------------------------\n"

"""
正则查找finding
"""
import re

sentence = "this is a test, not testing."
it = re.finditer('\\btest\\b', sentence)
for match in it:
    print "match position: " + str(match.start()) + "-" + str(match.end())

"""
查询数据库
"""
# db = MySQLdb.connect("localhost","username","password","dbname")
# cursor = db.cursor()
# sql = "select Column1,Column2 from Table1"
# cursor.execute(sql)
# results = cursor.fetchall()
#
# for row in results:
#     print row[0]+row[1]
#
# db.close()
print "----------------------------------------------------------\n"

"""
用指定分隔符连接列表list
"""
theList = ["a", "b", "c", "sfds", "b", "df", "a"]
joinedString = ",".join(theList)
print joinedString
print "----------------------------------------------------------\n"

"""
过滤掉字符串列表中的空字符串
"""
targetList = ["sdsf", "3e", "f3", "f", "  ", "", "fff", "dsfds"]
targetList1 = [v for v in targetList if not v.strip() == '']
print targetList1
# or
targetList2 = filter(lambda x: len(x) > 0, targetList)  # 不能过滤空格
print targetList2

print "----------------------------------------------------------\n"
"""
列表list相加
"""
newList = theList.extend(targetList)
print ("newlist: %s" % newList)
print "----------------------------------------------------------\n"

"""
遍历字典dict
"""
aDict = {"name": "guiping", "age": "12", "sex": "male"}
for k, v in aDict.iteritems():
    print k + ":" + v

print "----------------------------------------------------------\n"

"""
检查字符串是否存在于一个字符串列表中
"""
tstring = "f31"
if any(x in tstring for x in targetList):
    print "true"
else:
    print "false"
