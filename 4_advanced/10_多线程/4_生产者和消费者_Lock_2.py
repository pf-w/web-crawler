#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-09-23  20:39


import threading
import random
import time

gMoney = 1000
gLock = threading.Lock()
gTimes = 0
gTotalTimes = 10


class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gTimes
        while True:
            # if gTimes >= gTotalTimes:
            #     break
            gLock.acquire()
            money = random.randint(100, 1000)
            # gLock.acquire()
            if gTimes >= gTotalTimes:
                gLock.release()
                break
            gMoney += money
            print('%s生产了%d元钱，剩余%d元钱' % (threading.current_thread(), money, gMoney))
            print(gTimes)
            gTimes += 1
            gLock.release()
            time.sleep(0.5)


class Consumer(threading.Thread):
    def run(self):
        global gMoney
        while True:

            money = random.randint(100, 1000)
            gLock.acquire()
            if gMoney >= money:
                gMoney -= money
                print('%s消费了%d元，剩余%d元' % (threading.current_thread(), money, gMoney))
            else:
                if gTimes >= gTotalTimes:
                    gLock.release()
                    break

                print('%s消费者要消费%d元，还剩余%d，不足！' % (threading.current_thread(), money, gMoney))
            gLock.release()
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

