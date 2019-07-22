#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-08-30  15:35

"""
    反序列化：将json转换成python对象

    1、loads(str)：反序列化成python对象（list），str为要反序列化json

    2、load(fp)：从文件中的json反序列化
"""

import json


json_str = '[{"name": "tom", "age": 12}, {"name": "jerry", "age": 15}]'

strs = json.loads(json_str)

print(type(json_str))
print(type(strs))
print(strs)


print("="*30)

"""反序列化成python对象"""
with open("person_1.json", 'r', encoding='utf-8') as fp:
    s = json.load(fp)
    print(type(s))
    for i in s:
        print(i)
