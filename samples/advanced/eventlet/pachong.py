# -*- coding:utf-8-*-
"""
tutorial doc:
http://www.cnblogs.com/Security-Darren/p/4170031.html
http://eventlet.net/doc/basic_usage.html
"""
"""
客户端网络爬虫实例
"""

import eventlet
from eventlet.green import urllib2  # 引入绿化后的 urllib2

urls = ["http://www.rockytravel.net/wp-content/uploads/2014/01/BestPlacestotravelaloneAustralia.jpg",
        "http://wanderlustcrunch.com/wp-content/uploads/2014/07/origin_quotes-at-the-right-12-420x470.jpg",
        "http://aspiringbackpacker.com/wp-content/uploads/2012/01/Me-walking-alone-in-Wadi-Rum1.jpg",
        "http://www.theplaidzebra.com/wp-content/uploads/2015/05/2_traveling-alone-as-a-women.jpg",
        "http://s1.it.atcdn.net/wp-content/uploads/2014/03/solo-travel.jpg",
        "http://intelligenttravel.nationalgeographic.com/files/2014/09/skyline-drive-fall.jpg",
        "http://images2.fanpop.com/image/photos/9900000/Drive-the-Silk-Road-Istanbul-to-Beijing-travel-9932742-1029-683.jpg"]


def fetch(url):
    print("opening", url)
    body = urllib2.urlopen(url).read()
    print("done with", url)
    return url, body

# 创建一个绿色线程池，缺省容量为1000，线程池可以控制并发，限制内存消耗的上限；
pool = eventlet.GreenPool(200)
# 遍历并行调用函数 fetch 后的结果，imap 可以并行调用函数 fetch ，返回结果的先后顺序和执行的先后顺序相同。
for url, body in pool.imap(fetch, urls):
    print("got body from", url, "of length", len(body))
