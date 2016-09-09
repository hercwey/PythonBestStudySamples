# -*-coding:utf-8-*-
# ! /usr/bin/env python
'''
工作队列（又称任务队列——Task Queues）是为了“避免等待”一些占用大量资源和时间的操作。
下面我们将通过time.sleep()函数来模拟耗时操作

你需要打开三个终端，两个用来运行worker.py脚本，这两个终端就是我们的两个消费者（consumers）
第三个终端，用来发布新任务。

默认地，RabbitMQ会按顺序地把消息发送给每个消费者。平均每个消费者都会收到同等数量的消息。这种发送消息的方式叫做——轮训（round-robin）。

消息确认：
为了防止消息丢失，RabbitMQ提供了消息响应（acknowledgments）。消费者会通过一个ack（响应），
告诉RabbitMQ已经收到并处理了某条消息，然后RabbitMQ就会释放并删除这条消息。

如果消费者（consumer）挂掉了，没有发送响应，RabbitMQ就会认为消息没有被完全处理，然后重新发送给其他消费者（consumer）。这样，及时工作者（workers）偶尔的挂掉，也不会丢失消息。

消息是没有超时这个概念的；当工作者与它断开连的时候，RabbitMQ会重新发送消息。这样在处理一个耗时非常长的消息任务的时候就不会出问题了。

'''

import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

print('[*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print("[x] Received %r" % body)
    time.sleep(body.count(b'.'))  # 消息体中每一个点号（.）模拟1秒钟的操作
    print("[x] Done")
    ch.basic_ack(
        delivery_tag=method.delivery_tag)  # 一个很容易犯的错误就是忘了basic_ack，后果很严重。消息在你的程序退出之后就会重新发送，如果它不能够释放没响应的消息，RabbitMQ就会占用越来越多的内存。


'''
使用basic.qos方法，并设置prefetch_count=1,这样告诉RabbitMQ，在同一时刻，不要
发送超过1条消息给一个工作者（worker），直到它已经处理了上一条消息并作出了响应。
这样，RabbitMQ就会把消息分发给下一个空闲的工作者（worker）
'''
channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue='task_queue')

consuming = channel.start_consuming()
