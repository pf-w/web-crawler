#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-08-14  14:56

"""
    parse.urlencode(dict) 对url进行编码, 参数为dict类型, 转换成str类型
    pares.parse_qs(url) 对url进行解码, 返回字典类型

"""

from urllib import request
from urllib import parse    # 解码和编码都是在urllib.parse下的

# url = "https://www.baidu.com/s?wd=胡歌"

url = "https://www.baidu.com/s?"


d = {"wd": "胡歌"}

# 对url进行编码

"""
    urlencode : Encode a dict or sequence of two-element tuples into a URL query string.
"""
qs = parse.urlencode(d)     # 若对真个url进行编码，报错

print("类型：", type(qs))
print("urlencode: ", qs, end="\n\n")

url = url + qs

print(url)

request = request.urlopen(url=url)

# print(request.read().decode())

print(request.getcode(), end="\n\n")

# 对编码的url进行解码

result = parse.parse_qs(url)

print("parse_qs: ", result)
