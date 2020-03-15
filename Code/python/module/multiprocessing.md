multiprocessing支持子进程、通信和共享数据、执行不同形式的同步，提供了Process、Queue、Pool、Pipe、Lock等组件。

## [Process](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process)

```python
class multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
```

应该始终使用关键字参数调用构造函数

- group参数永远为None，该参数仅用于兼容`threading.Thread`
- target应该是一个可以调用的对象，它会被run()方法调用
- name是进程名
- args是target所调用方法的参数
- kwargs是target所调用方法的关键字参数
- daemon默认为None，意味着从创建进程中继承，可设为True(守护进程)或False(非守护进程) 

### start()

- 启动进程，只能调用一次，他会在进程中调用run方法

### join([*timeout*])

- 设主进程为m，子进程为s，m中调用s.join()：阻塞m，直到s进程结束，*timeout*是一个正数，它最多会阻塞timeout秒 ，另外，s.join()可调用若干次
- 一个进程p调用自己进程的join (p.join()) 可能会导致死锁【自己join自己这种骚操作不会，因此没实验】
- 只能在调用s.start()后调用s.join()

**join可防止产生僵尸进程，文档中的[编程指南](https://docs.python.org/3/library/multiprocessing.html#multiprocessing-programming)中指出：每次开启一个新进程，所有未被join的进程会被join（也就是说非守护进程会自动被join），但即便如此也要明确地join启动的所有进程。因此如果不手动地join子线程，主进程也会等待子进程中止之后再中止**

## Queue

```python
class multiprocessing.Queue([maxsize])
```

- qsize() 返回队列的大小 
- empty() 如果队列为空，返回True，反之False 
- full() 如果队列满了，返回True，反之False
- get([block[, timeout]]) 获取队列，timeout等待时间 
- get_nowait() 相当Queue.get(False)
- put(item) 写入队列，timeout等待时间 
- put_nowait(item) 相当Queue.put(item, False)



生产者和消费者问题

```python
# -*- coding: utf-8 -*-
import os
import time
import random
from multiprocessing import Queue, Process

class Processor(object):
    def __init__(self, nums_producer=1, nums_consumer=1):
        self.nums_producer = nums_producer
        self.nums_consumer = nums_consumer
        self.queue = Queue()
        self.producer_list = self.init_process(self.producer, self.nums_producer)
        self.consumer_list = self.init_process(self.consumer, self.nums_consumer)

    def init_process(self, target, nums):
        procs = []
        for _ in range(nums):
            p = Process(target = target)
            procs.append(p)
        return procs

    # 生产者
    def producer(self):
        for i in range(5):
            result = random.random()
            self.queue.put((os.getpid(), i))
            print('Producer: {} produce {}'.format(os.getpid(), i))
            time.sleep(0.5 * random.random())

    # 消费者
    def consumer(self):
        while True:
            pid, i = self.queue.get()
            print('Consumer: {} consume {} - {}'.format(os.getpid(), pid, i))
            time.sleep(0.5 * random.random())

    # 开启所有子进程
    def start(self):
        for process in self.producer_list:
            process.start()
        for process in self.consumer_list:
            process.start()

    # 等待所有子进程结束
    def join(self):
        for process in self.producer_list:
            process.join()
        for process in self.consumer_list:
            process.join()

if __name__ == "__main__":
    p = Processor(nums_producer = 3, nums_consumer = 2)
    p.start()
    p.join()
```

## 参考

- [官方文档](https://docs.python.org/3/library/multiprocessing.html)
- [Python3多进程multiprocessing模块的使用](https://www.jianshu.com/p/a5f10c152c20)
- [python中的Queue与多进程（multiprocessing）](https://my.oschina.net/yangyanxing/blog/296052)
- [python多进程——multiprocessing.Process](https://www.cnblogs.com/Magic-Dev/p/11420692.html)

