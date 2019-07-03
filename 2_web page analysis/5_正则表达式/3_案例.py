#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-08-28  16:48

"""
    使用正则表达式验证一些小案例
"""

import re

# 验证手机号
tel = "13415943721"
v0 = re.match("1[34578]\d{9}", tel)
print(v0)


print("="*50)


# 验证邮箱
email = "1011467276@qq.com"
v1 = re.match("\w+@[a-zA-Z0-9]+\.[a-z]+", email)
print(v1)


print("="*50)


# 验证url
url = "http://www.baidi.com/"
# v2 = re.match("(http|https|ftp)://[^\s]+", url)
v2 = re.match("(http|https|ftp)://.+", url)
print(v2)


print("="*80)


# 验证身份证号
id = "30332317611651651x"
v3 = re.match("\d{17}[\dxX]", id)
print(v3)
