#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-08-15  20:11

"""
    CookieJar --派生-->
        FileCookieJar --派生-->
            MozillaCookieJar 和 LWPCookieJar

    使用MozillaCookieJar("path") 和 save("path", ignore_discard) 进行保存cookie

    使用load("path", ignore_discard)进行加载保存的cookie

    ignore_discard=True 可以保存或加载过期的cookie
"""

from urllib import request, parse
from http.cookiejar import MozillaCookieJar


# 保存cookie
# 1、创建MozillaCookieJar("path")
# cookiejar = MozillaCookieJar("New_Folder/百度Cookie.txt")
cookiejar = MozillaCookieJar()  # 若在此处不指明路径，则save() 和 load() 都要指明

# 2、使用request.HTTPCookieProcessor(CookieJar())创建Handler
handler = request.HTTPCookieProcessor(cookiejar)

# 3、使用request.build_opener创建opener
opener = request.build_opener(handler)

# 4、请求网址
# req = request.Request(url="https://www.baidu.com")
# resp = opener.open(req)
#
# # 5、保存cookie
# cookiejar.save("New_Folder/百度Cookie.txt")    # 在创建MoaillaCookieJar对象时若指定path，则此处可不必在制定path
#
#
# # 加载cookie
# cookiejar.load("New_Folder/百度Cookie.txt")
# # print(cookiejar)
# for cookie in cookiejar:
#     print(cookie)


# ---------------------- 人人网Cookie ----------------------

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}

data = {
    "email": "17866673602",
    "password": "A1011467276"
}

req_2 = request.Request(url="http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2018732045118",
                        headers=headers, data=parse.urlencode(data).encode("utf-8"))
resp_2 = opener.open(req_2)

# 保存cookie
cookiejar.save("New_Folder/人人网Cookie.txt")

# 加载cookie
# cookiejar.load("New_Folder/人人网Cookie.txt")
# print("\n\n\n")
# for cookie in cookiejar:
#     print(cookie)

# ------------ 访问人人网 ------------
req_3 = request.Request(url="http://www.renren.com/880151247/profile",
                        headers=headers)

resp_3 = opener.open(req_3)

with open("New_Folder/人人网Cookie.html", "w", encoding="utf-8") as f:
    f.write(resp_3.read().decode("utf-8"))
