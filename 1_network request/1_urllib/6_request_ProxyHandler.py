#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-08-15  13:21

from urllib import request, parse

"""
    ---------------- IP代理 ----------------

    1——urllib.request.ProxyHandler是设置IP代理

    1、使用ProxyHandler（dict）传入一个ip代理，
       传入的值是字典格式，key是传输类型：http或https，
       值是“IP：port”格式

    2、使用request.build_opener（handler）构建一个opener，
       参数是构建的handler

    3、使用opener的open（url）发起请求

    使用urlopen实际上是封装了上述步骤

"""


url = "http://httpbin.org/ip"   # httpbin.org 可以查看http请求的参数


'''不使用代理'''
# resp = request.urlopen(url)
#
# print(resp.read().decode("utf-8"))



'''使用代理'''
# # 1、构建ProxyHandler
# handler = request.ProxyHandler({"http": "103.38.43.216:53281"})
#
# # 2、构建opener
# opener = request.build_opener(handler)
#
# # 3、使用open（）请求
# req = request.Request(url=url)
# resp = opener.open(req)
#
# print(resp.read())


print("------------- 用ip代理爬取拉钩 -------------")

lg_url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"

# 设置ip代理
# 1、使用urllib.request.ProxyHandler(dict{"method": "ip:port"})构建handler,参数为dict
handler = request.ProxyHandler({"http": "139.199.153.25:1080"})
# 2、使用urllib.request.build_opener(handler)构建opener
opener = request.build_opener(handler)
# 3、使用opener.open(url)请求

heasders = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Referer": "https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput="
}

data = {
    "first": "true",
    "pn": 1,
    "kd": "python"
}

req = request.Request(url=lg_url, headers=heasders,
                      data=parse.urlencode(data).encode("utf-8"))

resp = opener.open(req)

print("获得状态码：", resp.getcode())

print(resp.read().decode("utf-8"))
