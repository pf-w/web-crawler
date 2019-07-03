#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-08-18  19:04

import requests

# url = "http://www.baidu.com"

url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"

headers = {
    "Referer": "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}

data = {
    "first": "true",
    "pn": "1",
    "kd": "python"
}

# 代理
proxy = {
    "http": "180.118.73.2:9000"
}

resp = requests.post(url=url, headers=headers, data=data, proxies=proxy)
# resp = requests.post(url=url, headers=headers, data=data)

print(resp.json())

# with open("New_Folder/lagou.json", "w", encoding="utf-8") as f:
#     f.write(resp.content.decode("utf-8"))