#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-08-28  17:21

"""
    ^：以什么开始
    $：以什么结束
    |：匹配多个表达式

    【注意】：若匹配的同时存在^和$，就会匹配整个字符串
"""

import re

s0 = "123#skvjbkj"
r0 = re.match("^\d", s0)
print(r0)


s1 = "xxxxx@163.com"
r1 = re.match("\w+@163\.com$", s1)
print(r1)

url = "http://www.baidi.com/"
v2 = re.match("(http|https|ftp)://[^\s]+", url)
print(v2)


v3 = re.match("^123#skvjbkj$", s0)  # 若：用^和$表示以什么开头，并以什么结尾；表示匹配字符串
print(v3)

