#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-09-18  22:09

"""
    创建一个类，继承于threading.Thread类，并重写run()方法
"""

import threading
import time


class Walk(threading.Thread):
    def run(self):
        for i in range(3):
            print("walk_%s..." % threading.currentThread())
            time.sleep(1)

class Run(threading.Thread):
    def run(self):
        for i in range(3):
            print('run_%s...' % threading.current_thread())
            time.sleep(1)


def main():
    t1 = Walk()
    t2 = Run()

    t1.start()
    t2.start()

    print("所有线程信息:", threading.enumerate())


if __name__ == '__main__':
    main()
