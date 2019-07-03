#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-08-29  11:01

"""
    flags = re.DOTALL 表示 . 可以匹配所有字符，包括\n

    1、match()：从字符串的开头开始匹配，若开头不匹配，则返回None；即：只要开头不匹配就返回None

    2、search()：在字符串中查找匹配的字符，查到就返回

    3、findall()：匹配所有满足条件的结果，返回list

    4、sub(pattern, replace, str, count, flags)：匹配符合条件的字符串并替换, 返回替换后的字符串
        pattern: 正则表达式
        replace: 要替换成的字符串，
        str：    要替换的字符串
        count：  要替换几个，默认是替换所有
        flags：

    5、split(pattern, str)：以正则表达式分隔字符串，返回list

    6、compile()：compile()函数并不是匹配函数，必须借助其他匹配函数(match、search、findall、sub、split)，才能匹配

        【function_1】：compile()会把编译好的正则表达式放入内存，
                                这样在每次执行的时候不会重复编译，
                                如：r = re.compile("\d")
                                   res = re.match(r, str)
        【function_2】：compile()可以为正则表达式进行注释，须有参数，re.VERBOSE

                    如：re.compile(r'''
                                \d+   # 小数点前的数字
                                \.?   # 小数点
                                \d*   # 小数点后的数字
                                ''', re.VERBOSE)    【必须要有re,VERBOSE参数】

    7、group()及groups()： 分组函数，【见"7——分组_group()_groups().py"】

        ①、使用"()"对正则表达式进行分组

        ②、使用group()获取已经分组的正则表达式所匹配的字符
            group() 等价于 group(0)，获取的时整个正则表达式所匹配的内容，
                整个正则表达式也相当于一个大的分组
            group(1)可以获取到正则表达式中第一个使用"()"进行分组所匹配的结果
            group(2)类似于group(1)，以此类推
            group()可以传入多个参数：
                group(1,2)表示获取正则表达式中与第1个和第2个"()"位置相对应的匹配结果

        ③、groups()可以获取正则表达式中所有分组所匹配的结果
"""

import re

s = "Apple price is $10. Orange price is $12"

print("=================================== match() ===================================")

r0 = re.match("\w*", s)
r1 = re.match("\d", s)      # 若第一个字符不匹配，则返回None
print(r0)
print(r1)


print("\n================================== search() ===================================")
r2 = re.search("\$\d+", s)      # 查找到就返回
print(r2)


print("\n================================== findall() ==================================")
r3 = re.findall("\$\d+", s)     # 匹配所有符合条件的字符串
print(r3)


print("\n==================================== sub() ====================================")
r4 = re.sub("\$", "￥", s)               # sub(pattern, replace, str, count)
r5 = re.sub("\$", "￥", s, count=1)      # 替换正则表达式匹配的字符，并返回替换后的字符串
print(r4)
print(r5)


print("\n================================== split() ==================================")
r6 = re.split("\.", s)      # 以正则表达式匹配到的字符分隔开，并返回list
print(r6)


print("\n================================== compile() ==================================")
print("-------------- compile(pattern) --------------")
r = re.compile("\$\d+")     # 使用re.compile(pattern)只会编译一次，并存储到内存，下一次使用不会再编译
r7 = re.findall(r, s)
print(r7)


# 带注释的正则表达式
print("-------------- compile(pattern, re.VERBOSE) --------------")
r = re.compile("""
\$  # 匹配"$"
\d+ # 匹配数字
""", re.VERBOSE)

r8 = re.findall(r, s)
print(r8)