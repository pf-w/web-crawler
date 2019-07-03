#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-08-31  14:27

"""
    方法一：
        1、使用csv.writer(fp)创建伊格write对象，
        2、再使用writerow(value)写入一行或用writerows(value)写入多行

        【注意】：
            此方法写入的value必须是list 或 tuple

    方法二：
        1、使用csv.DictWriter(fp, header)创建write对象,
            fp为文件对象，headers是表头（标题栏那一行）
        2、使用writeheader()写入header，再上面只是传入参数，并没有写入文件
        3、使用writerows(value)写入多行数据或用writerow写入一行

        【注意】：
            1、此方法写入的value为dict
            2、必须调用writeheader(),手动写入表头

    【注意】：
        使用open()打开文件，每写入一行会自动加一个“\n”, csv中不允许有空行
        所以使用open()函数的newline属性指定一个空字符串，即：open(newline="")
"""


import csv


def writer_csv_demo():
    """使用writer写入文件"""
    header = ["name", "age"]
    value = [
        ('张三', 15),
        ("李四", 16),
        ("王五", 15)
    ]

    with open("write_csv.csv", 'w', encoding="utf-8", newline="") as fp:
        writer = csv.writer(fp)     # 创建writer对象
        writer.writerow(header)     # 写入表头信息
        writer.writerows(value)


def DictWriter_csv_demo():
    """使用DictWriter写入文件"""
    header = ["name", "age"]
    # value = [
    #     {'name': "张三", "age": 15},
    #     {'name': "李四", "age": 16},
    #     {'name': "王五", "age": 15}
    # ]
    value = [{'name': "张三", "age": 15}]

    with open("DictWriter_csv.csv", 'w', encoding="utf-8", newline="") as fp:
        writer = csv.DictWriter(fp, header)     # 传入文件对象和表头信息
        writer.writeheader()        # 把表头文件写入文件
        writer.writerows(value)     # 写入数据


if __name__ == '__main__':
    # writer_csv_demo()
    DictWriter_csv_demo()