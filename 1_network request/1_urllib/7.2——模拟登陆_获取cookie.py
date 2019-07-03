#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-08-15  15:47

"""
    模拟登陆人人网（自动获取Cookie）

    人人网登陆的url：http://www.renren.com/SysHome.do

    人人网测试的url：http://www.renren.com/967471160

    需要用到http.cookiejar.CookieJar 和
"""


# from 1——urllib import request, parse
# from http.cookiejar import CookieJar
#
# login_url = "http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2018731948829"
#
# # 1、获取登陆的Cookie, cookie会保存在opener中
# # 1.1、创建一个CookieJar对象
# cookiejar = CookieJar()
# # 1.2、用request.HTTPCookieProcessor(CookieJar())创建一个handler
# handler = request.HTTPCookieProcessor(cookiejar)
# # 1.3、用request.build_opener创建一个opener
# opener = request.build_opener(handler)
# # 1.4、用opener.open请求登陆页面，再次访问时不需要再建一个opener，
#        因为已经把cookie保存到opener中
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
# }
#
# data = {
#     "email": "17866673602",
#     "password": "A1011467276",
# }
#
# req = request.Request(url=login_url, headers=headers,
#                       data=parse.urlencode(data).encode("utf-8"))
#
# s = opener.open(req)
# print(s)
#
#
# # 2、模拟登陆
# url = "http://www.renren.com/967471160"
#
# req_1 = request.Request(url=url, headers=headers)
# rep = opener.open(req_1)
#
# with open("New_Folder/人人网_2.html", "w", encoding="utf-8") as f:
#     f.write(rep.read().decode("utf-8"))


print("--------------------------- 再来一遍 ---------------------------")


from urllib import request, parse
from http.cookiejar import CookieJar

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}


def get_cookie():
    """获取登陆需要的cookie"""

    # 先声明cookiejar对象
    cookiejar = CookieJar()
    # 通过request.HTTPCookieProcessor(CookieJar())创建handler
    handler = request.HTTPCookieProcessor(cookiejar)
    # 通过request.build_opener(Handler)创建一个opener
    opener = request.build_opener(handler)
    # 接下来请求页面
    return opener


def login(opener):
    """登陆"""

    data = {
        "email": "17866673602",
        "password": "A1011467276"
    }

    login_url = "http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2018731931971"
    req = request.Request(url=login_url, headers=headers,
                          data=parse.urlencode(data).encode("utf-8"))

    opener.open(req)


def visit(opener):
    """访问"""
    url = "http://www.renren.com/967471160"

    req = request.Request(url=url, headers=headers)
    resp = opener.open(req)
    with open("New_Folder/人人网_again.html", "w", encoding="utf-8") as f:
        f.write(resp.read().decode("utf-8"))
        print(type(resp.read()))


if __name__ == '__main__':
    opener = get_cookie()
    login(opener)
    visit(opener)
