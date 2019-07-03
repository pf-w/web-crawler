#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2019-04-03  17:14

"""
    selenium设置代理：（以Chrome浏览器为例）
        1、创建一个options
        options = webdriver.ChromeOptions()
        2、操作options设置代理
        options.add_argument("--proxy-server=http://110.52.235.57:9999")
        3、将options传入Chrome()中
        driver = webdriver.Chrome(chrome_options=options)
        Chrome()还有参数executable_path指定Chrome浏览器驱动的路径
"""

from selenium import webdriver

# 1、创建options
options = webdriver.ChromeOptions()

# 2、使用options指定ip代理
options.add_argument("--proxy-server=http://112.85.168.115:9999")

# 3、将options传入Chrome()中
# driver = webdriver.Chrome(chrome_options=options)
driver = webdriver.Chrome(options=options)  # DeprecationWarning: use options instead of chrome_options

# 访问页面
driver.get("https://httpbin.org/#/Request_inspection/get_ip")
