#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-08-30  14:43

"""
    序列化：将python对象转化成json字符串

    1、dumps(str)：序列化成json字符串,str为要反序列化的字符串

    2、dump(str, fp)：转储到json文件，str为反序列化的字符串，fp为文件路径或文件名
        若要转储的str有中文，需要再open()中指定编码，
        否则，将存储成Unicode字符串

    【dump —— 转储】
"""


import json


person = [
    {
        'name': 'tom',
        'age': 12
    },
    {
        'name': 'jerry',
        'age': 15
    }
]


"""序列化成json"""
json_str = json.dumps(person)

print(type(json_str))   # json本质上是str
print(type(person))

print("="*100)

print(json_str)     # 转换成json后，字符串变成了双引号


"""转储到文件"""
# 方法一
with open("person_1.json", 'w', encoding='utf-8') as fp:
    fp.write(json.dumps(person))
# 方法二
with open("person_2.json", 'w', encoding='utf-8') as fp:
    json.dump(person, fp)
