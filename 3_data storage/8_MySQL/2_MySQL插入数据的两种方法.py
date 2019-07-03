#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-09-01  15:22

"""
    1、给出sql语句   【Tip】pymysql底层中values的类型都是字符串，必须都用%s

    2、使用execute(sql, ())执行sql语句     【须传入一个tuple】
        参数：
            sql：要执行的sql语句
            (): 这个tuple是当sql语句没有指定具体values时，把变量放入tuple中

    3、使用connect.commit()映射到数据库
"""


import pymysql


def insert_method_1():
    """方法一"""

    # 创建连接
    connect = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password='root',
        database="crawl"
    )

    # 创建游标
    cursor = connect.cursor()

    sql = "insert into test(username,password) values ('张三','123')"

    # 使用游标执行插入操作
    cursor.execute(sql)

    # 映射到数据库，提交数据
    connect.commit()

    # 关闭数据库
    connect.close()


def insert_method_2():
    """方法二"""

    # 建立连接, port必须为整型
    connect = pymysql.Connect(
        host="localhost",
        port=3306,
        user="root",
        password='root',
        database="crawl"
    )

    # 创建游标
    cursor = connect.cursor()

    # 使用游标执行操作，
    # values中对应id的值为null
    #       因为MySQL中以设置id为自增，所以设置为null；也可以不设置id字段
    """以下都行"""
    # sql = "insert into test(id, username, password) values (null, %s,%s)"
    # sql = "insert into test(username, password) values (%s,%s)"
    sql = "insert into test values (null, %s,%s)"

    # username = "王五"
    # password = "112233"
    username = input("输入username ")
    password = input("输入password ")

    cursor.execute(sql, (username, password))

    connect.commit()

    connect.close()


if __name__ == '__main__':
    # insert_method_1()
    insert_method_2()

