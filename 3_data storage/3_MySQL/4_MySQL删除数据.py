#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-09-02  13:45

import pymysql

connect = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="123",
    database="spider"
)

cursor = connect.cursor()

sql = "delete from test where id=1"

cursor.execute(sql)

connect.commit()

connect.close()


