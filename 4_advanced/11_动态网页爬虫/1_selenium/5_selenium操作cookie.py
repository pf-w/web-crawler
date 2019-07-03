#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2019-04-01  15:35

"""
    get_cookies() : 获取所有的cookie

    get_cookie(key) : 获取key的cookie值

    delete_cookie(key) : 删除某个cookie值

    delete_all_cookies()  : 删除所有的cookie

"""

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

for cookie in driver.get_cookies():     # get_cookies() ：获取所有的cookie
    print(cookie)

print("="*30)

print(driver.get_cookie("BD_UPN"))      # 获取某个字段的cookie值

# driver.delete_cookie(key)     # 删除某个cookie值

# driver.delete_all_cookies(key)   # 删除所有的cookie
