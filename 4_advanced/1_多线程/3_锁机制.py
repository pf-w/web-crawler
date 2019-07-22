#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-09-20  22:04

"""

"""

import threading


VALUE = 0

glock = threading.Lock()    # 创建（定义）锁


def add_value():
    global VALUE    # 声明使用全局变量

    glock.acquire()     # 上锁    【acquire ：获得】

    for i in range(1000000):
        VALUE += 1

    glock.release()     # 关锁  【release ：释放】
    print(VALUE)


def thread_method():
    for i in range(2):
        t = threading.Thread(target=add_value)
        t.start()


if __name__ == '__main__':
    # main_1()
    # main_2()
    thread_method()

