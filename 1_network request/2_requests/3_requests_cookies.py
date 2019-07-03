#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-08-20  9:50

"""
    使用requests.cookies获取cookie

"""

import requests


# 获取人人网cookie
url = "http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2018731931971"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}

data = {
    "email": "17866673602",
    "password": "A1011467276"
}


response = requests.post(url, headers=headers, data=data)

print(response.cookies, end="\n\n\n")

# 将cookie转化成dict

print("------- 将cookies转换成dict -------\n", response.cookies.get_dict())