#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-09-02  13:55

import pymysql

connect = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="123",
    database="spider"
)

cursor = connect.cursor()

sql = "update test set password='asd' where username='李四'"

cursor.execute(sql)

connect.commit()

connect.close()
