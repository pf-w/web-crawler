#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-09-22  22:44
import random
import threading
import time

MONEY = 1000
LOCK = threading.Lock()

TotalTime = 10
initTime = 0

class Producer(threading.Thread):
    def run(self):
        global MONEY
        global initTime
        global TotalTime
        while True:
            if initTime >= TotalTime:
                break
            money = random.randint(100, 1000)
            LOCK.acquire()
            MONEY += money
            print('生产者%s生产了%d元，总共%d元' % (threading.current_thread(), money, MONEY))
            initTime += 1
            LOCK.release()
            time.sleep(1)



class Consumer(threading.Thread):
    def run(self):
        global MONEY
        while True:

            money = random.randint(100, 1000)
            if MONEY >= money:
                LOCK.acquire()
                MONEY -= money
                print('消费者%s消费了%d元，总共%d元' % (threading.current_thread(), money, MONEY))
                LOCK.release()
                time.sleep(1)
            else:
                if initTime >= TotalTime:
                    break
                print('消费%d元，总共%d元，余额不足！！！' % (money, MONEY))
                break

def main():

    # for i in range(2):
    #     p = Producer(name='生产者%d' % i)
    #     p.start()
    #
    # for i in range(3):
    #     c = Consumer(name='消费者%d' % i)
    #     c.start()

    for i in range(5):
        t = Producer(name="生产者%d"%i)
        t.start()

    for x in range(3):
        t = Consumer(name="消费者%d"%x)
        t.start()


if __name__ == '__main__':
    main()

