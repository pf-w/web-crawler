#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-08-31  13:25

"""
    1、使用csv.reader(fp)进行读取，返回迭代器，遍历迭代器时返回list，
        并包含标题栏那一行，若要去除标题栏则先调用迭代器中的next()方法

    2、使用csv.DictReader(fp)返回迭代器， 遍历迭代器时返回有序的dict类型，
       不包含标题栏那一行

    3、取特定的列时，reader(fp)使用下标, DictReader(fp)使用标题栏的具体字段
"""

import csv


def reader_csv_demo0():
    """包含标题栏的reader"""
    with open("Stock.csv", 'r') as fp:
        reader = csv.reader(fp)
        for i in reader:
            print(i)
        # print(type(reader))     # reader对象


def reader_csv_demo1():
    """不包含标题栏的reader"""
    with open("Stock.csv", 'r') as fp:
        reader = csv.reader(fp)
        next(reader)    # 读取了第一行的标题栏, 当再次遍历迭代器时，不会再包含标题栏
        for i in reader:
            print(i)


def reader_csv_demo2():
    """取特定的列"""
    with open("Stock.csv", 'r') as fp:
        reader = csv.reader(fp)
        for i in reader:
            print(i[0], "=====", i[3])


def DictReader_demo0():
    """使用DicitReader(fp)读取csv文件"""
    with open("Stock.csv", 'r') as fp:
        reader = csv.DictReader(fp)
        for i in reader:
            print(i)


def DictReader_demo1():
    """使用DictReader(fp)读取特定的列"""
    with open("Stock.csv", 'r') as fp:
        reader = csv.DictReader(fp)
        for i in reader:
            print(i['date'])


if __name__ == '__main__':
    # reader_csv_demo0()
    # reader_csv_demo1()
    # reader_csv_demo2()
    #
    # DictReader_demo0()
    DictReader_demo1()


