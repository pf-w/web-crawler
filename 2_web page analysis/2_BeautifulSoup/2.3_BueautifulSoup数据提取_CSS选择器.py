#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-08-26  10:23

"""
    BeautifulSoup使用CSS选择器：
        1、使用soup.select(ele)来使用css选择器   ele 为标签名

        2、使用css选择器只能提取标签，而不能提取属性和文本
            必须使用BeautifulSoup的相关语法才能提取标签的属性和文本

    【注意】：
        1、虽然使用的是css选择器，但是这里是基于BeautifulSoup使用的，
            所以使用select()和使用find_all()的功能是一样的，只是使用了不同的API

        2、使用css选择器（select()）和使用BeautifulSoup的find_all()方法类似，
            都不能像lxml中xpath()（xpath语法）一样一次性提取到属性值和文本，
            只能使用BeautifulSoup中的方法
"""

import __init__
from bs4 import BeautifulSoup

"""
    任务：
        1、提取所有的tr标签
        2、提取第二个tr标签
        3、提取clss为even的tr标签
        4、获取所有a标签的href属性
        5、获取所有的文本信息
"""

# 构建一个BeautifulSoup对象
soup = BeautifulSoup(__init__.text, "lxml")

# 1、提取所有的tr标签
# trs = soup.select("tr")     # 返回list
# for tr in trs:
#     print(tr)       # tr为Tag类型
#     print("="*50)


# 2、提取第二个tr标签
# tr = soup.select("tr")[1]
# print(tr)


# 3、提取clss为even的tr标签
# # # trs = soup.select("tr.even")
# # trs = soup.select(".even")
# trs = soup.select("tr[class=even]")
# for tr in trs:
#     print(tr)


# test
a = soup.select(".h, #s")       # 获取类名为h的 或 id为s的标签，不一定同时成立
for i in a:
    print(i)
    print('='*30)


# 4、获取所有a标签的href属性
# aList = soup.select('a')
# for a in aList:
#     href = a['href']      # 如同数组中的下标
#     print(href)


# # 5、获取所有的文本信息
# trs = soup.select("tr")[1:]
# for tr in trs:
#     textGenerator = tr.stripped_strings  # 返回生成器
#     text = list(textGenerator)
#     print(text)
#     print('='*50)
