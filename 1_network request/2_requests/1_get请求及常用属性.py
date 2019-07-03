#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-08-17  20:45

import requests


"""
    requests常用属性：
        0、requests.get(url, headers, params)
        1、requests.text: 返回str类型字符串, requests会根据自己的猜测自动编码
        2、requests.content: 返回byte类型的字符串, 
            从网络获取或从硬盘中取出的都是bytes类型的字符串，可以用decode()进行手动解码
        3、requests.url: 返回请求的url
        4、requests.encoding: 返回编码方式
        5、requests.status_code: 返回状态码
        
    
    
    requests.text和request.content的区别：
        requests.text会根据自己的猜测进行编码，返回的是str类型的字符串、
        requests.content不会进行编码，返回的是bytes字符串，可手动进行解码 
        
"""

response = requests.get("http://www.baidu.com")

"""验证类型"""
# print(type(response.text))
# print(type(response.content))
# print(isinstance(response.text, str))
# print(isinstance(response.content, bytes))

"""输出requests自动编码的内容"""
# print(response.text)


"""输出编码格式"""
print(response.encoding)    # 输出编码格式

"""可以使用.encoding进行指定编码"""
response.encoding="utf-8"   # 可以使用.encoding进行指定编码格式
# print(response.text)
print(response.encoding)    # 进行指定编码后，就会输出指定的编码

"""输出requests不会编码的内容"""
# print(response.content)

"""为content指定编码"""
# print(response.content.decode("utf-8"))     # 将bytes字符串解码成Unicode字符串


"""输出请求的url"""
print(response.url)


"""输出请求状态码"""
print(response.status_code)



'''
    进行get请求，get(url, headers, params), params为request请求中的查询字符串
        类型为字典，requests底层已经设计好，不需要对params进行编码，
        
        get()中为params、
        post()为data
'''


# 比如要查询“中国”，url应为"http://www.baidu.com/s？wd=中国"
url = "http://www.baidu.com/s"

params = {"wd": "中国"}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}


resp = requests.get(url=url, params=params, headers=headers)
print(resp.content.decode("utf-8"))
