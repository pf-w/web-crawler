#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-09-02  13:14


"""
    MySQL查询数据的三种方法：
        1、fetchone()    返回一条数据

        2、fetchall()    返回所有查询的数据

        3、fetchmany(size)   返回指定数目的数据，size为要查询的数目


        【fetch：取来】
"""


import pymysql


def fetchone_demo():
    connect = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        database="crawl"
    )

    cursor = connect.cursor()

    sql = "select * from test where id=1"

    cursor.execute(sql)

    # fetchone
    result = cursor.fetchone()

    print("fetchone:\n", result)

    connect.close()


def fetchall_demo():
    connect = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="root",
        database="crawl"
    )

    cursor = connect.cursor()

    sql = "select * from test"

    cursor.execute(sql)

    result = cursor.fetchall()

    print("fetchall:\n", result)

    connect.close()


def fetchmany_demo():
    connect = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        database="crawl"
    )

    cursor = connect.cursor()

    sql = "select * from test"

    cursor.execute(sql)

    result = cursor.fetchmany(2)

    print("fetchmany:\n", result)

    connect.close()


if __name__ == '__main__':
    fetchone_demo()
    fetchall_demo()
    fetchmany_demo()
