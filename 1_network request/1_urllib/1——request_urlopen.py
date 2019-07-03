#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-08-14  13:48


from urllib import request

"""
    urlopen(url, data, timeout, ...) 默认使get请求，若加入headers信息则为post请求
    
    urlopen的返回值使http.client.HTTPRespose对象
    
    urlopen不能设置请求头
"""

rsp = request.urlopen(url="http://www.baidu.com")



if __name__ == "__main__":

    print(rsp.getcode(), end="\n\n")    # 获取请求码

    # print(rsp.read())

    print(rsp.read().decode("utf-8"))   # 读取内容，并进行解码
