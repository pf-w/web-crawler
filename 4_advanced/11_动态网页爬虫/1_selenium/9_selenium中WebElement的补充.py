#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2019-04-06  14:32


from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebElement

# driver继承于Webdriver,Webdriver继承于RemoteWebDriver，RemoteWebDriver继承于WebDriver
driver = webdriver.Chrome()

driver.get("https://www.baidu.com")

submitBut = driver.find_element_by_id("su")

print(submitBut)    # 返回WebElement对象
# 得到标签的属性
print(submitBut.get_attribute("value"))

# 保存截图，并不是在标签元素上，而是在driver上，此文件是以png格式
driver.save_screenshot("pic/baidu.png")     # 将截图保存到pic/baidu.png
