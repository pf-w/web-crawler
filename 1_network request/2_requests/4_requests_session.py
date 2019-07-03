#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-08-20  10:01

"""
    用requests.session()获取cookie

    cookie会保存在session中


    1、先创建session对象
    2、通过session对象去请求页面, cookie会保存在session中, 下一次请求页面直接用session去请求
        类似于urllib库中的opener，cookie会保存在opener中一样

    此处用requests.session()和requests.Session()作用相同
"""

import requests

url = "http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2018731931971"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}

data = {
    "email": "17866673602",
    "password": "A1011467276"
}

"""
    通过session获取cookie
"""
# 使用requests.session()
session = requests.Session()    # 创建session对象

resp = session.post(url, headers=headers, data=data)   # cookie会保存在session中
# 打印一下cookies
print(resp.cookies)
with open("New_Folder/人人网.jaon", 'w', encoding='utf-8') as f:
    f.write(str(resp.cookies))

# 用session去请求页面
visit_url = "http://www.renren.com/880151247/profile"

response = session.get(visit_url)

with open("New_Folder/人人网_test.html", "w", encoding="utf-8") as f:
    f.write(response.content.decode("utf-8"))
