#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-09-18  21:29

"""
    使用多线程模块threading， threading模块python自带

    使用threading模块：
        t = threading.Thread(target)    # target指定要执行的函数
        t.start()   # 启动线程

        threading.enumerate(): 返回所有的线程
        threading.current_thread(): 返回当前线程信息
        threading.currentThread(): 同current_thread() 返回当前线程信息
"""

import threading
import time


def walk():
    for i in range(3):
        print("walk_%s...>>>" % threading.current_thread())
        time.sleep(1)   # 睡眠1秒

def run():
    for i in range(3):
        print('run_%s...' % threading.currentThread())
        time.sleep(1)


def main_1():
    '''使用单线程'''
    walk()
    run()

def main_2():
    """使用多线程"""
    t1 = threading.Thread(target=walk)
    t2 = threading.Thread(target=run)

    t1.start()
    t2.start()

    print("所有线程:", threading.enumerate())   # 一共有3个线程：main、t1、t2


if __name__ == '__main__':
    # main_1()  # 单线程
    main_2()    # 多线程


"""
    threading.Thread(target).start()     创建并启动线程
    threading.current_thread()   返回当前线程信息
    threading.currentThread()   返回当前线程信息
    threading.enumerate()   返回所有线程信息
"""


