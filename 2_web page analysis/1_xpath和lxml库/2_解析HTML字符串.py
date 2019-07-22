#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-08-21  11:57

from lxml import etree
import __init__

"""
    使用lxml.etree对HTML字符串进行解析
    1、先创建一个etree.HTML()对象
    2、通过etree.tostring(htmlEle, encode)进行解析   
        etree.tostring(htmlEle, encode)会自动加上body和html标签
     
"""



# print(text)

htmlEle = etree.HTML(__init__.text)  # 返回一个Element对象，可以用这个对象去执行xpath

print(type(htmlEle))

html = etree.tostring(htmlEle, encoding="utf-8")

print(type(html))

print(html.decode("utf-8"))

