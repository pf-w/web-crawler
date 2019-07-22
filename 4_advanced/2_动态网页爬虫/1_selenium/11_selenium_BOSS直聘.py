#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2019-04-07  19:58

from selenium import webdriver
import re, time


class Boss():
    url = "https://www.zhipin.com/c100010000/?query=python&ka=sel-city-100010000"
    # url = "https://www.zhipin.com/c100010000/?query=python&page=10"
    driver = webdriver.Chrome()

    def __init__(self):
        self.url = Boss.url
        self.driver = Boss.driver
        # self.domain = "https://www.zhipin.com"

    def get_page_url(self):
        self.driver.get(self.url)
        while True:
            detail_urls = re.findall('<div class="info-primary">.*?href="(.*?)"', self.driver.page_source, re.DOTALL)
            for detail_url in detail_urls:
                url = "https://www.zhipin.com" + detail_url
                try:
                    self.get_detail(url)
                except:
                    continue
                time.sleep(1)
                # return
            # next_page_class = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[3]/div[3]/a[last()]')
            next_page_class = self.driver.find_element_by_css_selector('#main>div>div.job-list>div.page>a.next')
            if "disabled" in next_page_class.get_attribute("class"):
                self.driver.quit()
                return
            next_page_class.click()
            time.sleep(1)

    def get_detail(self, page_url):
        self.driver.execute_script("window.open('{}')".format(page_url))
        self.driver.switch_to.window(self.driver.window_handles[1])


        # 职位名称
        position_name = self.driver.find_element_by_css_selector(".name h1").text
        # 薪资
        salary = self.driver.find_element_by_css_selector(".salary").text
        # 职位信息
        position_info = self.driver.find_element_by_xpath('//*[@id="main"]/div[1]/div/div/div[2]/p').text

        re_str = re.compile("[点击地图|查看全部|竞争力分析|综合竞争力评估|你在？位置|一般|良好|优秀|极好查看完整个人竞争力|个人综合排名：|在|人中排名第]")

        # 职位描述
        job_describe = self.driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]').text
        job_describe = re.sub(re_str, "", job_describe)
        # 公司介绍
        company_info = self.driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[3]').text
        company_info = re.sub(re_str, "", company_info)
        # 团队
        team = self.driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[2]').text
        team = re.sub(re_str, "", team)
        # 工商信息
        information = self.driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[5]').text
        information = re.sub(re_str, "", information)
        # 地址
        address = self.driver.find_element_by_class_name('location-address').text

        print(position_name, salary, position_info, end="\n")
        print(job_describe)
        print(team)
        print(company_info)
        print(information)
        print("地址：" + address)

        print("="*80, end="\n")

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])


if __name__ == '__main__':
    boss = Boss()
    boss.get_page_url()

