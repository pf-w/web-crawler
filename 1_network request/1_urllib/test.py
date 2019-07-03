#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-08-14  17:59


# class A():
#     def a(self):
#         print("a")
#
# class B(A):
#     def a(self):
#         # super(B, self).a()
#         print("b")
#
# class C(A):
#     def a(self):
#         # super(C, self).a()
#         print("c")
#
# class D(B, C):
#     def a(self):
#         super(D, self).a()
#         print("d")
#
# d = D()
# print(D.mro())
# d.a()


from urllib import request,parse
from http.cookiejar import MozillaCookieJar

url = "http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2018732045118"
visit_url = "http://www.renren.com/880151247/profile"



data = {
    "email": "17866673602",
    "password": "A1011467276"
}


cookiejar = MozillaCookieJar("aaa.txt")

handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}

req = request.Request(url=url, headers=headers,
                      data=parse.urlencode(data).encode("utf-8"))

opener.open(req)

# cookiejar.save()

cookiejar.load("aaa.txt", ignore_discard=True, ignore_expires=True)

req_2 = request.Request(url=visit_url, headers=headers)

resp = opener.open(req_2)

with open("aaa.html", "w", encoding="utf-8") as f:
    f.write(resp.read().decode("utf-8"))