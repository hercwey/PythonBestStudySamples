#!/usr/bin/env python
# -*-coding:utf-8-*-
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

# RabbitMQ中，消息不能直接发送到队列，它需要发送到交换机（exchange）中
channel.basic_publish(exchange='', routing_key='hello', body='RabbitMQ, Hello World!!!')

print("[x] Sent 'RabbitMQ, Hello World!'")

connection.close()
