#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2019-04-01  13:50

"""
    常见的表单元素：
        input标签，type可以是：text、password、email、number
        按钮：button、input[type是submit]
        选择框：checkbox、input[type是checkbox]
        下拉列表：select

    clear会清空输入框

    在下拉列表中，select元素不能直接点击，
    因为点击后还需要选择元素，这时候selenium就专门为select标签提供了一个类
    selenium.webdriver.support.ui import Select
    将获取的元素当成参数传到这个类中，创建这个对象，以后就可以使用这个对象进行选择
    示例代码如下：
        from selenium.webdriver.support.ui import Select

        # 选中这个标签，然后使用Select创建一个对象
        select_tag = Select(driver.find_element_by_name("jumpMenu"))\

        # 根据索引进行选择
        select_tag.select_by_index(1)

        # 根据值进行选择
        select_tag.select_by_value("https://www.baidu.com")

        # 根据可视的文本进行选择
        select_tag.deselect_by_visible_text("*****")

        # 取消选中的所有选项
        select_tag.deselect_all()

"""

from selenium import webdriver
import time


driver = webdriver.Chrome()

"""文本框"""

# driver.get("https://www.baidu.com")
#
# input_tag = driver.find_element_by_id("kw")
#
# input_tag.send_keys("python")   # 给input标签填充字段
#
# time.sleep(2)
#
# input_tag.clear()   # 清空input框

"""按钮"""
# driver.get("https://www.baidu.com")
#
# input_tag = driver.find_element_by_id("kw")
#
# input_tag.send_keys("python")   # 给input标签填充字段
#
# time.sleep(2)
#
# submit_tag = driver.find_element_by_id("su")    # 找到按钮
#
# submit_tag.click()  # 点击按钮

"""选择框"""

# driver.get("https://account.geekbang.org/signup?redirect=https%3A%2F%2Fs.geekbang.org%2F")
#
# remember = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/p[1]/input')
#
# time.sleep(2)
# remember.click()    # 勾选checkbox
#
# time.sleep(2)
#
# remember.click()    # 取消勾选checkbox

"""下拉列表"""
from selenium.webdriver.support.ui import Select
driver.get("https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/select")

# 选中标签，并创建Select对象
select_tag = Select(driver.find_element_by_id("language"))

# 使用索引操作下拉列表
# select_tag.select_by_index("1")

# 使用value操作下拉列表
# select_tag.select_by_value("/en-US/docs/Web/HTML/Element/select")

# 使用text操作下拉菜单
select_tag.select_by_visible_text("English (US) (en-US)")
