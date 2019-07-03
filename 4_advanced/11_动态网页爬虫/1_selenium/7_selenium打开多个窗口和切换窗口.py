#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2019-04-03  16:30

"""
    1、打开多窗口：
        打开多个窗口需要使用driver.execute_script(str_JavaScript),
        通过JavaScript来实现打开，但driver还停留在原来的窗口上
    2、窗口之间的切换：
        打开另一个窗口以后，driver仍然停留在原来的窗口上，可以用
        driver.switch_to_window(driver.window_handles[num]) # 此方法已经弃用，改为switch_to.window(...)
        来切换driver所在的窗口

        driver.window_handles表示的是窗口句柄，是一个list

    3、可以用driver.current_url查看driver所在的当前页面
    4、可以用driver.page_source查看当前页面的代码
"""

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")

print("创建新窗口之前driver所在的窗口：", driver.current_url)

driver.execute_script("window.open('https://douban.com')")  # 通过JavaScript打开另一个窗口

print("创建新窗口之后driver所在的窗口：", driver.current_url)

# 使用窗口句柄切换driver所在的窗口, 此方法已经弃用，改为：switch_to.window
# driver.switch_to_window(driver.window_handles[1]) # window.handles是一个list
driver.switch_to.window(driver.window_handles[1])   # 1 代表是第二个打开的窗口

print("切换窗口之后driver所在的窗口：", driver.current_url)

print("\n\n"+driver.page_source)


