#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-09-23  21:56


"""
    Lock版的生产者和消费者可以正常运行，
    但是存在一个不足：在消费者中通过while死循环并且上锁的方式判断生产者生产的够不够
    上锁是一个很消耗cpu资源的行为，因此这种方式不是最好的；
    通过threading.Condition可以解决，

    threading.Condition可以在没有数据的时候处于阻塞状态，
    一旦有了数据，可以使用notify()或notify_all()相关函数来通知其他处于等待状态的线程
    这样就可以省去一些不必要的上锁操作

    threading.Condition()相关函数：
        acquire(): 上锁；
        release(): 解锁；
        wait(): 将当前线程处于等待状态，并会释放锁；
                可以使用notify()或notify_all()函数进行唤醒，
                被唤醒后会继续等待上锁，上锁后继续执行下面的代码
        notify(): 通知某个等待的线程（wait操作等待的线程）可以继续执行，默认是第一个等待的线程
        notify_all(): 通知所有等待的线程可以继续执行

        【注意】：notify()和notify_aal()不会自动释放锁，并且需要在release()之前进行调用


        wait()：将当前线程置为等待状态，并释放通过acquire()加的锁

        notify(): 通知被wait()阻塞的某个线程（通常是第一个）可以继续执行，不会释放锁，要使用release()释放
        notify_all()： 通知被wait()阻塞的所有线程可以继续执行，不会释放锁，要使用release()释放

        【notify : 通知】
"""


import threading
import time
import random

condition = threading.Condition()   # threading.Condition()使用的是threading.Lock()

gMoney = 1000
gTimes = 0
gTotalTimes = 10


class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gTimes
        while True:
            # if gTimes >= gTotalTimes:
            #     break
            condition.acquire()     # 上锁
            money = random.randint(100, 1000)
            # gLock.acquire()
            if gTimes >= gTotalTimes:
                condition.release()
                break
            gMoney += money
            print('%s生产了%d元钱，剩余%d元钱' % (threading.current_thread(), money, gMoney))
            print(gTimes)
            gTimes += 1
            condition.notify_all()      # 通知所有的线程可以继续执行，并释放锁
            condition.release()     # 释放锁
            time.sleep(0.5)


class Consumer(threading.Thread):
    def run(self):
        global gMoney
        while True:

            money = random.randint(100, 1000)
            condition.acquire()     # 上锁

            while gMoney < money:
                if gTimes >= gTotalTimes:
                    condition.release()     # 释放锁
                    return
                condition.wait()        # 阻塞线程

            gMoney -= money
            print('%s消费者要消费%d元，还剩余%d' % (threading.current_thread(), money, gMoney))
            condition.release()     # 释放锁
            time.sleep(0.5)


def main():

    for i in range(5):
        t = Producer(name="生产者%d"%i)
        t.start()

    for x in range(3):
        t = Consumer(name="消费者%d"%x)
        t.start()


if __name__ == '__main__':
    main()




