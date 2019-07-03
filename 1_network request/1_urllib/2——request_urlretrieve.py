#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-08-14  14:12

from urllib import request

"""
    urlretrieve()是将网页中的文件保存到本地
    
    url retrieve : retrieve —— 取回
"""

rsp = request.urlretrieve(url="http://www.baidu.com", filename="New_Folder\\baidu.html")

