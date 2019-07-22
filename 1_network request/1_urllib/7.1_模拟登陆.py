#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-08-15  15:47

"""
    模拟登陆人人网（简单粗暴）

    人人网url：http://www.renren.com

    Cookie为登陆后Request Headers中的Cookie
"""


from urllib import request


url = "http://www.renren.com"

# Cookie为登陆后Request Headers中的Cookie
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Cookie": "anonymid=jkute9x4-tiv8ce; depovince=GW; _r01_=1; ick_login=694407e2-6523-4797-a952-d4585abc06b1; ick=4404fb31-feb4-4a8e-9dc5-6822b623547e; t=017427465201cc85474177e8be6c01590; societyguester=017427465201cc85474177e8be6c01590; id=967471160; xnsid=c36ef3a9; JSESSIONID=abcmmIlbCDwizcdWtK8uw; ver=7.0; loginfrom=null; jebe_key=b9932d0e-f70d-41b9-bb4c-7a7ef831c0c5%7C7e7761ce8a579cd3df348e7465e953cc%7C1534319478054%7C1%7C1534319482078; wp_fold=0; jebecookies=8a929d9e-8c3d-4b8a-b432-40278d1c19f3|||||"
}

req = request.Request(url=url, headers=headers)

resp = request.urlopen(req)

# 写入文件
with open("New_Folder/人人网.html", "w", encoding="utf-8") as f:
    f.write(resp.read().decode("utf-8"))
