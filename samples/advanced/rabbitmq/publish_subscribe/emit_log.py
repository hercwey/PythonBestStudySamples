# -*-coding:utf-8-*-
# ! /usr/bin/env python
'''
在上篇教程中，我们搭建了一个工作队列，每个任务只分发给一个工作者（worker）。在本篇教程中，我们要做的跟之前完全不一样 —— 分发一个消息给多个消费者（consumers）。这种模式被称为“发布／订阅”。
为了描述这种模式，我们将会构建一个简单的日志系统。它包括两个程序——第一个程序负责发送日志消息，第二个程序负责获取消息并输出内容。
在我们的这个日志系统中，所有正在运行的接收方程序都会接受消息。我们用其中一个接收者（receiver）把日志写入硬盘中，另外一个接受者（receiver）把日志输出到屏幕上。
最终，日志消息被广播给所有的接受者（receivers）。

'''
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs', routing_key='', body=message)
print("[x] Sent %r" % message)
connection.close()
