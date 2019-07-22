#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-09-04  13:36

import pymongo


"""
    MongoDB的使用
    
    1、连接MongoDB：
        使用pymongo.MongoClient(host, port)创建连接MongoDB的对象 
            host: 主机名或ip
            port: 27017     【Tip】port和MySQL一样必须是整型
            
        client = pymongo.MongoClient(host, port)
            
    2、指定数据库：
        使用创建的连接MongoDB的对象指定要操作的数据库
        db = client.DATABASE
        【Tip】DATABASE可以不存在
    
    3、指定集合：
        使用创建的数据库对象指定要操作的集合
        collection = db.COLLECTION
        
    4、MongoDB的增删改查
        使用创建的集合对象操作MongoDB
        
        增：
            <1> 使用 collection.insert(value)        插入一条数据
            <2> 使用 collection.insert_one(value)    插入一条数据
            <3> 使用 collection.insert_many(values)  插入多条数据
            
            
        删：
            <1> 使用collection.delete_one(条件)     删除一条数据
            <2> 使用collection.delete_many(条件)    删除多条数据
            
            
        改：
            <1> 使用collection.update_one({条件}, {"$set":{value}})  修改一条数据
            <2> 使用collection.updata_many({条件}, {"$set":{value}}) 修改多条数据
            
            
        查：
            <1> collection.find_one()       查找第一条数据, 返回dict
            <2> collection.find_one(条件)    根据条件查找一条数据, 返回dict
            <3> collection.find()           查找多条数据, 返回Cursor对象
            <4> collection.find(条件)        根据条件查找多条数据
            
            
        【Tip】：
            1、插入的数据是一个字典形式
            
            2、插入多条数据时参数为tuple或list，即要插入的数据放在list或tuple中   
           
            3、增删改查的过程相当于在cmd中输入的命令
            
"""


# 创建连接MongoDB对象
cline = pymongo.MongoClient(host="localhost", port=27017)

# 使用mongodb对先指定数据库
db = cline.my_test      # 此处指定的数据库可以不存在，若不存在则创建，如同 “use 数据库名”

# 使用指定的逐句库指定集合
collection = db.test


"""以下是MongoDB的增删改查"""

# ------------------------------- 增 -------------------------------
# 插入一条数据
# collection.insert({"username":"李四", "age":10, "grade":78})
# collection.insert_one({"username": "嘿哈", "age": 9, "grade": 98})

# 插入多条数据（参数中必须是list或tuple）
# collection.insert_many(
#     [
#         {"username": "王五", "age": 9, "grade": 80},
#         {"username": "二傻子", "age": 10, "grade": 89}
#     ]
# )


# ------------------------------- 改 -------------------------------
# 修改一条数据
# collection.update({"username":"aaa"}, {"$set":{"username":"王麻子"}})
# collection.update_one({"username":"王麻子"}, {"$set":{"username":"aaa"}})

# 修改多条数据
# collection.update_many({"age":10}, {"$set":{"age":8}})


# ------------------------------- 查 -------------------------------
# 查找一条数据
# result = collection.find_one()
# print(result)
# print(type(result))

# 根据条件查找一条数据
# result = collection.find_one({"username":"嘿哈"})
# print(result)

# 查找所有数据
# cursor = collection.find()
# print(type(cursor))
# for i in cursor:
#     print(i)

# 根据条件查找多条数据
# cursor = collection.find({"age":9})
# for i in cursor:
#     print(i)


# ------------------------------- 删 -------------------------------

# collection.delete_one({"username":"aaa"})
# collection.delete_many({"age":9})

# # collection.delete_many() 报错, 不能使用delete和delete_many()删除所有document
