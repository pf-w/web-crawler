#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2019-04-01  15:20


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

input_tag = driver.find_element_by_id('kw')
submit_tag = driver.find_element_by_id('su')

action = ActionChains(driver)   # 创建行为链

action.move_to_element(input_tag)   # 光标移动到input_tag上
action.send_keys_to_element(input_tag, "python")    #
action.move_to_element(submit_tag)
action.click(submit_tag)
action.perform()

