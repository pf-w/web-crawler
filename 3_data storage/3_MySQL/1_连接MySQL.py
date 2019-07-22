#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-09-01  14:20

"""
    1、使用pymysql.connect()创建一个连接，
            主要参数：
                host:主机名或ip
                port: 端口号   【必须为整型】
                user：用户名
                password：密码
                database：数据库名

    2、用cursor()创建游标
    3、使用游标进行增删改查操作
    4、使用close()关闭数据库
"""

import pymysql


# 1、使用pymysql.connect()创建一个连接
connect = pymysql.Connect(
    host="localhost",
    port=3306,
    user="root",
    password='root',
    database="crawl"
)

# 2、使用connect.cursor()创建游标
cursor = connect.cursor()

# 3、使用cursor对数据库进行操作
cursor.execute("select 1")

result = cursor.fetchone()

print(result)

# 4、使用connect.close()关闭数据库
connect.close()
