#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-08-24  13:42

"""
    使用BeautifulSoup进行解析

    BeautifulSoup的底层是用解析器去解析页面的
        常用的解析器有：html.parser(默认)、lxml、 html5lib
        html.parser: python内置，速度适中，容错力强
        lxml：速度快，容错能力强，但必须先安装C语言库 即：安装lxml即可 【最常用】
        html5lib: 容错性最好，以浏览器的方式解析，不需要外部扩展，但速度慢


    1、导入
        from bs4 import BeautifulSoup
    2、对html进行解析
        bs = BeautifulSoup(str, parser) parser为解析器

    3、使用prettify进行打印    prettify：美化
"""

import __init__
from bs4 import BeautifulSoup

bs = BeautifulSoup(__init__.text, "lxml")   # 返回bs4.BeautifulSoup对象

print(type(bs))
# 打印 prettify: 美化
print(bs.prettify())
