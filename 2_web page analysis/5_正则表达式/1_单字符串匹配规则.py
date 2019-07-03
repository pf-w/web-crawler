#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-08-28  10:47


import re

"""
    match()会从第一个匹配，若第一个不匹配，则返回None
"""


h = "hello"
s = "1123"
s_1 = "asc"
w = "_"
W = "*"
s_2 = "\n"
s_3= " "
s_4 = "\t"
s_5 = "\r"
s_6 = "\f"


"""匹配普通字符串"""
rh_1 = re.match('he', h)
rh_2 = re.match('el', h)    # 从开头进行匹配
print(rh_1)
print(rh_2)


print("="*50)


"""\d：匹配数字"""
rd_0 = re.match("\d", s)
rd_1 = re.match('\d', s_1)
print(rd_0)
print(rd_1)
# 使用group获得匹配的字符, 若为None则报错
print(rd_0.group())


print('='*50)


"""\D：匹配非数字"""

rD_0 = re.match('\D', s)
rD_1 = re.match('\D', s_1)

print(rD_0)
print(rD_1)


print('='*50)


"""\w：匹配字母、数字、下划线; a-z、A-Z、0-9、_"""


rw_0 = re.match("\w", s)
rw_1 = re.match("\w", s_1)
rw_2 = re.match("\w", w)

print(rw_0)
print(rw_1)
print(rw_2)


print('='*50)


"""\W：匹配非字母、数字、下划线"""
rW_0 = re.match("\W", s)
rW_1 = re.match("\W", s_1)
rW_2 = re.match("\W", w)
rW_3 = re.match("\W", W)

print(rW_0)
print(rW_1)
print(rW_2)
print(rW_3)


print('='*50)


""".：匹配除换行符之外的任何字符"""
r_0 = re.match('.', s)
r_1 = re.match('.', w)
r_2 = re.match('.', W)
r_3 = re.match('.', s_2)

print(r_0)
print(r_1)
print(r_2)
print(r_3)


print('='*50)


"""\s：匹配空白字符"""
rs_0 = re.match('\s', s_2)
rs_1 = re.match('\s', s_3)
rs_2 = re.match('\s', s_4)
rs_3 = re.match('\s', s_5)
rs_4 = re.match('\s', s_6)
print(rs_0)
print(rs_1)
print(rs_2)
print(rs_3)
print(rs_4)


print('='*50)


"""[]代替\d"""
r0 = re.match("[0-9]", s)
r1 = re.match("[0-9]", s_1)

print(r0)
print(r1)


print('='*50)


"""[]代替\D"""
r2 = re.match("[^0-9]", s)
r3 = re.match("[^0-9]", s_1)

print(r2)
print(r3)


print('='*50)


"""[]代替\w"""
r_4 = re.match("[A-Za-z0-9_]", s)
r_5 = re.match("[A-Za-z0-9_]", s_1)
r_6 = re.match("[A-Za-z0-9_]", w)
r_7 = re.match("[A-Za-z0-9_]", W)

print(r_4)
print(r_5)
print(r_6)
print(r_7)


print('='*50)


"""[]代替\W"""
r_8 = re.match("[^A-Za-z0-9_]", s)
r_9 = re.match("[^A-Za-z0-9_]", s_1)
r_10 = re.match("[^A-Za-z0-9_]", w)
r_11 = re.match("[^A-Za-z0-9_]", W)

print(r_8)
print(r_9)
print(r_10)
print(r_11)



