# -*- coding:utf-8-*-
from __future__ import print_function
import eventlet
"""
tutorial doc:
http://www.cnblogs.com/Security-Darren/p/4170031.html
http://eventlet.net/doc/basic_usage.html
"""
"""
简单服务器实例

这个简单的服务器实例监听端口 7000，响应每一个用户输入，
运行该文件启动该服务器，

通过执行：
  telnet localhost 7000

连接到它，可以通过终止 telnet 断开连接(通常 Ctrl-] 然后 'quit')
"""



def handle(fd):
    print("client connected")
    while True:
        # pass through every non-eof line
        x = fd.readline()
        if not x:
            break
        fd.write(x)
        fd.flush()
        print("server echoed", x, end=' ')
    print("client disconnected")

print("server socket listening on port 7000")
server = eventlet.listen(('0.0.0.0', 7000))
pool = eventlet.GreenPool()
while True:
    try:
        new_sock, address = server.accept()
        print("accepted", address)
        pool.spawn_n(handle, new_sock.makefile('rw'))
    except (SystemExit, KeyboardInterrupt):
        break

"""
程序解释:
server = eventlet.listen(('0.0.0.0', 6000)) 一句创建一个监听套接字；
pool = eventlet.GreenPool(10000) 一句创建一个绿色线程池，最多可以容纳10000个客户端连接；
new_sock, address = server.accept() 一句很特殊，由于这里创建的服务器套接字是经过绿化的，所以当多个连接到来时在accept()这里不会阻塞，而是并行接收；
pool.spawn_n(handle, new_sock) 一句为每一个客户端创建一个绿色线程，该绿色线程不在乎回调函数 handle 的执行结果，也就是完全将客户端套接字交给回调 handle 处理。
"""
