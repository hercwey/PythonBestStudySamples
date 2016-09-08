#!/usr/bin/env python
# -*-coding:utf-8-*-
import pika

# 建立一个到RabbitMQ服务器的阻塞连接
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# 从连接中获取一个channel通道
channel = connection.channel()

channel.queue_declare(queue='hello')

# 当接收到消息的时候，pika库就会调用此回调函数。
def callback(ch, method, properties, body):
    print("[x] Received %r" % body)

# 告诉RabbitMQ，回调函数将从名为hello的队列中接收消息
channel.basic_consume(callback, queue='hello', no_ack=True)

print('[*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
