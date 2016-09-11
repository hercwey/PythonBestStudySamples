# -*-coding: utf-8-*-
'''
tutorial: http://www.cnblogs.com/vman/p/5555559.html
sys模块提供了一系列有关Python运行环境的变量和函数。
'''

import sys

'''
sys.argv
可以用sys.argv获取当前正在执行的命令行参数的参数列表(list)。
变量 	解释
sys.argv[0] 	当前程序名
sys.argv[1] 	第一个参数
sys.argv[2] 	第二个参数
实例运行：
python sys_module.py arg1 arg2 arg3
'''

# 获取脚本名字
print 'The name of this program is: %s' % (sys.argv[0])
# 获取参数列表
print 'The command line arguments are:'
for i in sys.argv:
    print i
# 统计参数个数
print 'There are %s arguments.' % (len(sys.argv) - 1)

'''
sys.platform
获取当前执行环境的平台，如win32表示是Windows 32bit操作系统，linux2表示是linux平台；
'''
print sys.platform

'''
sys.path
path是一个目录列表，供Python从中查找第三方扩展模块。在python启动时，sys.path根据内建规则、PYTHONPATH变量进行初始化。
'''
print sys.path

'''
sys.builtin_module_names
sys.builtin_module_names返回一个列表，包含内建模块的名字。如：
'''
print sys.builtin_module_names

'''
sys.exit(n)
调用sys.exit(n)可以中途退出程序，当参数非0时，会引发一个SystemExit异常，从而可以在主程序中捕获该异常。
'''
print 'running...'
try:
    sys.exit(1)
except SystemExit:
    print 'SystemExit exit 1'
print 'exited'
