#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-08-14  15:53

"""
    urlparse 和 urlsplit 使分割url

    区别在于urlsplit有params, params不常用
"""

from urllib import parse

url = "https://www.baidu.com/p?wd=123&s=abc#a"  # 举栗子
url2 = "https://www.baidu.com/p;AAA?wd=123&s=abc#a"

result_0 = parse.urlparse(url)
result_1 = parse.urlsplit(url)

print("--- urlparse ---", parse.urlparse(url2), end="\n\n")
print("--- urlparse ---", result_0, end="\n\n")
print("--- urlsplit ---", result_1, end="\n\n")

print("类型：", type(result_1), end="\n\n")

print("--------------- urlparse ---------------")
print("scheme: ", result_0.scheme)
print("netloc: ", result_0.netloc)
print("path: ", result_0.path)
print("params: ", result_0.params)
print("query: ", result_0.query)
print("fragment:", result_0.fragment)

print("\n--------------- urlsplit ---------------")
print("scheme: ", result_1.scheme)
print("netloc: ", result_1.netloc)
print("path: ", result_1.path)
print("query: ", result_1.query)
print("fragment:", result_1.fragment)


