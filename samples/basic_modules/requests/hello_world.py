# -*-coding:utf-8-*-
# tutorial doc: http://docs.python-requests.org/zh_CN/latest/user/quickstart.html
import requests

r = requests.get('https://github.com/timeline.json')

print('status code: %s' % r.status_code)
print('response : %s' % r.text)
print('response json: %s' % r.json())
print('response raw: %s' % r.raw)
print('response header: %s' % r.headers)

### url 参数
# get
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)
print("url get: %s" % r.text)

# post
r = requests.post('http://httpbin.org/post', data=payload)
print("url post: %s" % r.text)

# url 传入list参数
payload = {'key1': 'value1', 'key2': ['value2', 'value3']}

r = requests.get('http://httpbin.org/get', params=payload)
print("url list param get: %s" % r.text)

# 定制请求头
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
print("header get: %s" % r.text)

# post 文件
'''
url = 'http://httpbin.org/post'
files = {'file': open('report.xls', 'rb')}
r = requests.post(url, files=files)
r.text
'''

# cookie
url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)
print('Cookie: %s' % r.cookies)

# 要想发送你的cookies到服务器，可以使用 cookies 参数：
url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
r.text

# 重定向
r = requests.head('http://github.com', allow_redirects=True)
print('url: %s' % r.url)
print('url: %s' % r.history)

# 超时
requests.get('http://github.com', timeout=0.001)
