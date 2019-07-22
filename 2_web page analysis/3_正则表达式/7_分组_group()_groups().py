#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-08-29  10:15

"""
    分组：
        1、使用"()"对正则表达式进行分组

        2、使用group()获取已经分组的正则表达式所匹配的字符
            group() 等价于 group(0)，获取的时整个正则表达式所匹配的内容，
                整个正则表达式也相当于一个大的分组
            group(1)可以获取到正则表达式中第一个使用"()"进行分组所匹配的结果
            group(2)类似于group(1)，以此类推
            group()可以传入多个参数：
                group(1,2)表示获取正则表达式中与第1个和第2个"()"位置相对应的匹配结果

        3、groups()可以获取正则表达式中所有分组所匹配的结果
"""

import re

s = "Apple price is $10. Orange price is $12"

r = re.search(".*(\$\d+).*(\$\d+)", s)

print("group()    : ", r.group())
print("group(0)   : ", r.group(0))      # group(0) 等价于 group(), 整个正则表达式也相当于一个大的分组
print("group(1)   : ", r.group(1))
print("group(2)   : ", r.group(2))
print("group(1,2) : ", r.group(1, 2))   # 获取对应"()"位置1、位置2的匹配结果

print("\ngroups()   : ", r.groups())    # 获取所有分组的匹配结果

