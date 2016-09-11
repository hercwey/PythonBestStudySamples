# -*-coding:utf-8-*-
#tutorial doc: http://docs.python-requests.org/zh_CN/latest/user/quickstart.html
import requests

r = requests.get('https://github.com/timeline.json')

print('status code: %s' % r.status_code)
print('response : %s' % r.text)
print('response json: %s' % r.json())
print('response raw: %s' % r.raw)

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

