#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-08-14  16:35

from urllib import request, parse

"""
    request.Request()可以设置请求头，但还是要借助urlopen()
    
    拉钩网
"""

url = "https://www.lagou.com/jobs/positionAjax.json?xl=%E5%A4%A7%E4%B8%93&px=default&needAddtionalResult=false"

# 对于有反爬虫的网站不能爬去真正的数据

# resp = request.urlopen(url)
#
# print(resp.read().decode("utf-8"))


# 用request.Request(url, headers, data, ...)进行请求

# 设置headers

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Referer": "https://www.lagou.com/jobs/list_python?px=default&xl=%E5%A4%A7%E4%B8%93&city=%E5%85%A8%E5%9B%BD"
}

data = {
    "first": "true",
    "pn": 2,
    "kd": "python"
}

req = request.Request(url=url, headers=headers, method="POST",
                      data=parse.urlencode(data).encode("utf-8"))

resp = request.urlopen(req)

print("获得状态码：", resp.getcode())

print(resp.read().decode("utf-8"))



