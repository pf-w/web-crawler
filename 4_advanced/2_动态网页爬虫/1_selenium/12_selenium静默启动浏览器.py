#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2019-04-07  22:48

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("headless")

driver = webdriver.Chrome(options=options)

driver.get("https://www.baidu.com")

print(driver.page_source)
