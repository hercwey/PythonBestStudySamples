# -*-coding:utf-8-*-
# ! /usr/bin/env python
'''
工作队列（又称任务队列——Task Queues）是为了“避免等待”一些占用大量资源和时间的操作。
下面我们将通过time.sleep()函数来模拟耗时操作

注意: 工作队列中每一条消息只能发送给其中一个客户端.
'''

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

"""
为了不让队列消失，需要把队列声明为持久化（durable）
将消息设为持久化并不能完全保证不会丢失。
以上代码只是告诉了RabbitMq要把消息存到硬盘，但从RabbitMq收到消息到保存之间还是有一个很小的间隔时间。
因为RabbitMq并不是所有的消息都使用fsync(2)——它有可能只是保存到缓存中，并不一定会写到硬盘中。
并不能保证真正的持久化，但已经足够应付我们的简单工作队列。如果你一定要保证持久化，
你需要改写你的代码来支持事务（transaction）。
"""
channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"

channel.basic_publish(exchange='', routing_key='task_queue', body=message,
                      properties=pika.BasicProperties(delivery_mode=2, ))  # make message persistent

print "[x] Sent %r" % (message,)
connection.close()
