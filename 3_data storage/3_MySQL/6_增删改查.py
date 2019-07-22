#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-09-02  14:12


import pymysql

class MySQL(object):
    connect = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        database="crawl"
    )

    cursor = connect.cursor()

    def insert(self):
        """增"""
        sql = "insert into test values (null, '二傻子', '000')"
        self.cursor.execute(sql)

        self.connect.commit()

        self.connect.close()

    def delete(self):
        """删"""
        sql = "delete from test where id=6"
        self.cursor.execute(sql)
        a = self.connect.commit()
        print(a)
        self.connect.close()

    def update(self):
        """改"""
        sql = "update test set username='嘿哈' where id=5"
        self.cursor.execute(sql)
        self.connect.commit()
        self.connect.close()

    def select(self):
        """查"""
        sql = "select * from test"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        print(result)
        self.connect.close()


if __name__ == '__main__':
    mysql = MySQL()
    # mysql.insert()
    # mysql.delete()
    mysql.update()
    mysql.select()

