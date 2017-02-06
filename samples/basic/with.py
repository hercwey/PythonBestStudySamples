#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: Hercwey
@license: Apache Licence 
@contact: 29053631@qq.com
@site: 
@software: PyCharm
@file: with.py
@time: 2017/2/6 16:16
"""

"""
tutorial: http://python.jobbole.com/82494/
with 语句适用于对资源进行访问的场合，确保不管使用过程中是否发生异常都会执行必要的“清理”操作，释放资源，
比如文件使用后自动关闭、线程中锁的自动获取和释放等。

要使用 with 语句，首先要明白上下文管理器这一概念。有了上下文管理器，with 语句才能工作。

上下文管理协议（Context Management Protocol）：包含方法 __enter__() 和 __exit__()，支持该协议的对象要实现这两个方法。

上下文管理器（Context Manager）：支持上下文管理协议的对象，这种对象实现了__enter__() 和 __exit__() 方法。上下文管理器定义执行 with 语句时要建立的运行时上下文，
负责执行 with 语句块上下文中的进入与退出操作。通常使用 with 语句调用上下文管理器，也可以通过直接调用其方法来使用。

运行时上下文（runtime context）：由上下文管理器创建，通过上下文管理器的 __enter__() 和__exit__() 方法实现，__enter__() 方法在语句体执行之前进入运行时上下文，__exit__() 在
语句体执行完后从运行时上下文退出。with 语句支持运行时上下文这一概念。

上下文表达式（Context Expression）：with 语句中跟在关键字 with 之后的表达式，该表达式要返回一个上下文管理器对象。

语句体（with-body）：with 语句包裹起来的代码块，在执行语句体之前会调用上下文管理器的 __enter__() 方法，执行完语句体之后会执行 __exit__() 方法。
"""

"""
清单 1. with 语句的语法格式
with context_expression [as target(s)]:
    with-body
"""

"""
清单 2. 使用 with 语句操作文件对象
with open(r'somefileName') as somefile:
    for line in somefile:
        print line
        # ...more code

这里使用了with语句，不管在处理文件过程中是否发生异常，都能保证with语句执行完毕后已经关闭了打开的文件句柄。
如果使用传统的try/finally范式，则要使用类似如下的代码：

清单 3. try/finally 方式操作文件对象
    somefile = open(r'somefileName')
    try:
        for line in somefile:
            print line
            # ...more code
    finally:
        somefile.close()

比较起来，使用with语句可以减少编码量。已经加入对上下文管理协议支持的还有模块threading、decimal等。
"""

"""
清单 4. with 语句执行过程

context_manager = context_expression
exit = type(context_manager).__exit__
value = type(context_manager).__enter__(context_manager)
exc = True  # True 表示正常执行，即便有异常也忽略；False 表示重新抛出异常，需要对异常进行处理
try:
    try:
        target = value  # 如果使用了 as 子句
        with-body  # 执行 with-body
    except:
        # 执行过程中有异常发生
        exc = False
        # 如果 __exit__ 返回 True，则异常被忽略；如果返回 False，则重新抛出异常
        # 由外层代码对异常进行处理
        if not exit(context_manager, *sys.exc_info()):
            raise
finally:
    # 正常退出，或者通过 statement-body 中的 break/continue/return 语句退出
    # 或者忽略异常退出
    if exc:
        exit(context_manager, None, None, None)
        # 缺省返回 None，None 在布尔上下文中看做是 False

"""