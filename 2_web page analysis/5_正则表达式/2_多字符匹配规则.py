#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-08-28  15:23

"""
    match()会从字符串一开始进行匹配，若字符串的第一个不符合，则返回None
"""

import re


""" ? 匹配0个或1个字符"""
r0 = re.match("\d?", "123a456")
# print(r0.group())
print(r0)


print("="*50)


"""+: 匹配至少一个字符"""
r1 = re.match("\w+", "asfzc++123")
r2 = re.match("\w+", "*asfzc++123")
print(r1)
print(r2)


print("="*50)


"""*: 匹配0或多个字符"""
r3 = re.match("\d*", "132@aa")
r4 = re.match("\d*", "#132@aa")  # 可以匹配0个，多以不会返回None
print(r3)
print(r4)


print("="*50)


"""{n}: 匹配n个字符"""
r5 = re.match("\d{2}", "123456798")
print(r5)


print("="*50)


"""{m,n}: 匹配m-n个字符, 【m和n之间不能有空格】"""
r6 = re.match("\d{2,5}", "159357123")   # 此为贪婪匹配
print(r6)


print("="*50)

