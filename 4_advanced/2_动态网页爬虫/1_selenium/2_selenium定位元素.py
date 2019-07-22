#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2019-04-01  11:07

"""
第一种方法：

    find_element_by_id  ： 根据元素的id定位元素

    find_element_by_class_name  : 根据又元素的class定位元素

    fing_element_by_name  : 根据name属性的定位元素

    find_element_by_tag_name  : 根据标签名定位元素

    find_element_by_xpath  : 根据xpath语法定位元素

    find_element_by_css_selector  : 根据css选择器定位元素

    【以上字段中的element是定位一个标签，elements是定位所有标签】
    【以上方法返回WebElement对象】

第二种方法:

    from selenium.webdriver.common.by import By

    find_element(By.CSS_SELECTOR, "#kw")

    send_keys ：给input填充字段

"""


from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.remote.webdriver import WebElement

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")

# 查找id为kw的元素
# input_tag = driver.find_element_by_id("kw")

# 查找class为s_ipt的元素
# input_tag = driver.find_element_by_class_name("s_ipt")

# 查找属性name为wd的元素
# input_tag = driver.find_element_by_name("wd")

# 通过xpath获取元素
# input_tag = driver.find_element_by_xpath('//input[@id="kw"]')

# 通过css选择器获取元素
# input_tag = driver.find_element_by_css_selector("#kw")

"""
使用第二种方法：
"""
# 通过class选区标签
input_tag = driver.find_element(By.CLASS_NAME, "s_ipt")

# 为input标签填充字段
input_tag.send_keys("python")
