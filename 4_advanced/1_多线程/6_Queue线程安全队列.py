#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-09-24  15:58

"""
    Queue是一个线程安全的队列，（python中提供的List不是线程安全的）
        线程安全表现在：线程具有原子性
        在queue中一个线程要么不执行，要么执行完再去执行其他线程
        可以实现线程同步

    1、从queue中导入Queue模块

    2、使用Queue([size])创建一个队列, size为可选参数，若没有size，则queue为变长

    3、对队列进行操作
        qsize(): 返回队列元素个数
        empty(): 判断队列是否为空
        full():  判断队列是否为满
        put(block=True): 向队列末尾添加数据  【默认是阻塞的】
                            当线程已到达最大数据量，再次放入数据时，就会变成阻塞状态，
                            直到有数据出队列，即：队列中有空闲位置
        get(block=True): 从队列开头取出数据  【默认是阻塞的】
                            当队列中没有数据，，使用get()去取数据时，线程就会变成阻塞状态，
                            直到队列中存在数据
"""
from queue import Queue
import time
import threading


# q = Queue()   # 若Queue(size)中指定size，则表示创建的队列的大小
#
# q.put(1)
# q.put(1)
# q.put(1)
# q.put(1)
# q.put(1)
#
# print(q.qsize())     # 打印元素的个数

value = 0

def put_value(q):
    print("-------")
    global value
    while True:
        q.put(value)
        value += 1
        if value > 5:
            break
        time.sleep(1)

def get_value(q):
    print("#######")
    while True:
        if value > 5:
            break
        print(q.get())

def main():
    q = Queue()
    p = threading.Thread(target=put_value, args=[q])    # 若指定的线程函数有参数，使用args传递list或tuple
    g = threading.Thread(target=get_value, args=[q])    # args是指定要传入的参数，用list后tuple

    p.start()
    g.start()

if __name__ == '__main__':
    main()