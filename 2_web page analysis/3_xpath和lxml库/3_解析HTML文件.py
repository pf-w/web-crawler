#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-08-21  13:12

"""
    利用etree.parse(file_source, [parser])进行对html文件的解析
    解析是不会自动添加html和body标签

    1、etree.parse(file_source, [parser])返回的是Element对象，
        可以使用Element对象执行xpath语句

    2、etree.parse()默认是XML的解析器，可以指定parser参数进行指定解析器
        HTMLParser

    3、etree.parse()默认的时xml的解析器，当html代码不太规范时，解析就会出错
        可以构造一个解析器对象，并传入etree.parse()中解决
        parser = etree.HTMLParser(encoding="utf-8")
        etree.parse(fileSource, parser=parser)

"""

from lxml import etree


def parse_tencent_file():
    file = "New_Folder/Tencent.html"
    htmlElement = etree.parse(file)  # 当html代码格式不规范时就会报错，下一个方法改进
    print(htmlElement)


def parse_lagou_file():
    """
    1、先构造一个解析器对象，并传入编码格式
    2、将解析器对象传入etree.parse()中
    :return:
    """
    file = "New_Folder/Lagou.html"

    # 构建解析器对象, 传入编码格式
    parser = etree.HTMLParser(encoding="utf-8")
    # 将解析器对象传入etree.parse()中
    htmlElement = etree.parse(file, parser=parser)
    print(etree.tostring(htmlElement, encoding="utf-8").decode("utf-8"))

if __name__ == '__main__':
    # parse_tencent_file()
    parse_lagou_file()