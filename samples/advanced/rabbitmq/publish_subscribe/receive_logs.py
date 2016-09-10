# -*-coding:utf-8-*-

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

#当与消费者（consumer）断开连接的时候，这个队列应当被立即删除。exclusive标识符即可达到此目的。
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)

print('[*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print("Received [x] %r" % body)


channel.basic_consume(callback, queue=queue_name, no_ack=True)

channel.start_consuming()
