#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-08-30  15:51

"""
    json中默认只能包含python中的基本数据类型
        （int、float、str、boolean、list、tuple、dict）

    若要包含类中的变量则使用方法返回, 再放入要转换成json的字符串
"""

import json

class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age


def get_attrs(s):
    return {
        'name': s.name,
        'age': s.age
    }


s = Student("张三", 15)

json_0 = json.dumps(get_attrs(s))

print(json_0)

