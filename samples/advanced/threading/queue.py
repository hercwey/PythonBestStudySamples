# -*-coding: utf-8 -*-
"""
 Python的Queue模块中提供了同步的、线程安全的队列类，包括FIFO（先入先出)队列Queue，LIFO（后入先出）队列LifoQueue，和优先级队列PriorityQueue。
 这些队列都实现了锁原语，能够在多线程中直接使用。可以使用队列来实现线程间的同步。
Queue模块中的常用方法:
    Queue.qsize() 返回队列的大小
    Queue.empty() 如果队列为空，返回True,反之False
    Queue.full() 如果队列满了，返回True,反之False
    Queue.full 与 maxsize 大小对应
    Queue.get([block[, timeout]])获取队列，timeout等待时间
    Queue.get_nowait() 相当Queue.get(False)
    Queue.put(item) 写入队列，timeout等待时间
    Queue.put_nowait(item) 相当Queue.put(item, False)
    Queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
    Queue.join() 实际上意味着等到队列为空，再执行别的操作
"""
import Queue
import threading
import time

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print "Starting " + self.name
        process_data(self.name, self.q)
        print "Exiting " + self.name


def process_data(threadName, q):
    print "Starting to process data..."
    while not exitFlag:
        # 处理队列时获取锁，处理完毕，释放锁
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print "%s processing %s" % (threadName, data)
        else:
            queueLock.release()
        time.sleep(1)


threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = Queue.Queue(10)
threads = []
threadID = 1

# 创建新线程
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

time.sleep(2)
# 填充队列（这时为何要获取锁？）
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
    print("queue size now: %s" % workQueue.qsize())
print("queue size: %s" % workQueue.qsize())
queueLock.release()

# 等待队列处理完毕（这里很关键）
while not workQueue.empty():
    #    print "The work queue is not finished, go on processing..."
    pass

print "\nNow the work queue has been finished to process, notify the threads to exit"
# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    print "\nWaiting all threads to finish...\n"
    t.join()

print "Now all sub threads finished, the main thread will be going to exit"
print "Exiting Main Thread"
