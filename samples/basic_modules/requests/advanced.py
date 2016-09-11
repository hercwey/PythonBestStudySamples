# -*-coding:utf-8-*-
# tutorial doc: http://docs.python-requests.org/zh_CN/latest/user/advanced.html#advanced
import requests

#会话session
'''
会话对象让你能够跨请求保持某些参数。它也会在同一个 Session 实例发出的所有请求之间保持 cookie，
期间使用 urllib3 的 connection pooling 功能。
所以如果你向同意主机发送多个请求，底层的 TCP 连接将会被重用，从而带来显著的性能提升。
'''
# 代码略

# SSL证书验证
'''
Requests 可以为 HTTPS 请求验证 SSL 证书，就像 web 浏览器一样。
要想检查某个主机的 SSL 证书，你可以使用 verify 参数:
'''
requests.get('https://kennethreitz.com', verify=False)

requests.get('https://github.com', verify=True)



