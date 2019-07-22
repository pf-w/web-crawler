#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2019-04-01  16:18

"""
    隐式等待：在获取元素之前先等待一段时间，再获取；若未获取到则报错
            调用driver.implicitly_wait

    显示连接：显示等待是表明某个条件成立之后才执行获取元素的操作。
            也可以在等待的时候指定一个最大的时间，如果超过这个时间就会抛出异常
            显示等待使用selenium.webdriver.support.excepted_conditions期望的条件
            和selenium.webdriver.support.WebDriverWait来配合完成

            即：若有要获取的元素立即返回，若找不到，则等待自定义的时间

            【
                若在显示连接中使用By.XPATH(使用xpath)时，只能到某个标签，
                而不能到具体的信息，如标签
                错误：presence_of_element_located((By.XPATH, "//div[@class='fl']/text()"))
            】
"""

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")


"""隐式等待"""
def YinShi():
    driver.implicitly_wait(10)  # 等待10秒的时间
    print(driver.find_element_by_id("kzhgvb;"))


"""显式等待"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def XianShi():
    element = WebDriverWait(driver, 10).until(
        # EC.presence_of_all_elements_located((By.ID, "skhvbklbfv"))
        EC.presence_of_element_located((By.ID, "kw"))  # 如果这里使用xpath只能获取到标签，不能到具体的信息，如文本
    )
    print(element)


if __name__ == '__main__':
    # YinShi()
    XianShi()









