#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-08-20  10:36

"""
    不信任的SSL证书：当访问https的网站时，证书可能是自己发布的，不被CA认可
    会在https前有一个“❌”

    在请求不信任的网站时，要加一个参数：verify=False, verify——校验
"""
import requests

url = "此处是证书没有被CA认证的网站的url"
# url = "https://www.baidu.com"

resp = requests.get(url, verify=False)

print(resp.content.decode("utf-8"))
