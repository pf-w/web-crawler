#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2019-04-01  10:57

"""
    driver.close() : 关闭当前页面

    driver.quit()  : 直接退出浏览器

"""


from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

# driver.close()    # 关闭当前页面

driver.quit()       # 关闭浏览器


