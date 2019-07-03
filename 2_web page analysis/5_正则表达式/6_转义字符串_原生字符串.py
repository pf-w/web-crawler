#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-08-28  21:59


import re


s = "price $299"
r = re.search("\$\d+", s)   # $在正则表达式中属于特殊字符，匹配字符串中的$时需要转义
print(r)


print("="*50)


s0 = "\n"   # 在python中\n代表换行，所以需要转义字符进行转义
r0 = re.match("\\n", s0)    # 匹配 \n(换行符)
print(r0)


print("="*50)


"""不使用python中的raw字符串"""
s1 = "\\n"   # 在python中\n代表换行，所以需要转义字符进行转义
r1 = re.match("\\\\n", s1)    # 匹配 \\n  正则表达式的\也是转义字符所以\\表示一个普通的\
print(r1)
print(s1)
print(r1.group())


print("="*50)


"""使用python中的raw字符串"""
s2 = r"\n"
r2 = re.match(r"\\n", s2)   # 正则表达式中\也为转义字符，所以使用\\表示一个普通的转义字符
print(r2)
print(r2.group())

