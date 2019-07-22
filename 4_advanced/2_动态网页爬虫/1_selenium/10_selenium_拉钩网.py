#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2019-04-06  16:39

from selenium import webdriver
import re, time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LaGou(object):
    driver = webdriver.Chrome()
    url = "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36",
    #     "Referer": "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=",
    #     "Cookie": "JSESSIONID=ABAAABAAAGFABEF03163941EDE23A36E63902F20A2C0B3A; user_trace_token=20190407145111-c314bbb5-65f7-4a68-8a9f-e3e38fc13b29; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1554619871; _ga=GA1.2.1314050992.1554619871; _gat=1; _gid=GA1.2.1082105677.1554619871; LGSID=20190407145112-880dc7f6-5901-11e9-88eb-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_python%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D; LGUID=20190407145112-880dcbee-5901-11e9-88eb-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_search; X_MIDDLE_TOKEN=08741b43a865e87b43ab0ff1e3325828; X_HTTP_TOKEN=d65e756b121290193989164551ab5c4760cdad6b18; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1554619892; LGRID=20190407145133-9474616a-5901-11e9-88ec-5254005c3644; SEARCH_ID=ad2f476942344176ac2770652157955f"
    # }
    # data = {
    #     "first": "false",
    #     "pn": "1",
    #     "kd": "python"
    # }
    def __init__(self):
        self.url = LaGou.url
        # self.hesders = LaGou.headers
        # self.data = LaGou.data
        self.driver = LaGou.driver

    def get_page(self):
        # options = webdriver.ChromeOptions()
        # options.add_argument("--proxy-server=http://121.232.148.81:9000")
        # self.driver = webdriver.Chrome(options=options)
        pn = 2
        self.driver.get(self.url)
        while True:
            source = self.driver.page_source
            # print(source)
            self.get_detail_url(source)

            time.sleep(1)

            try:
                # next_button = self.driver.find_element_by_xpath('//*[@id="s_position_list"]/div[2]/div/span[6]')
                next_button = self.driver.find_element_by_xpath('//*[@id="order"]/li/div[4]/div[2]')
                # if "pager_next_disabled" in next_button.get_attribute("class"):
                #     return
                next_button.click()
                self.data['pn'] = pn
                pn += 1
            except:
                break

            time.sleep(1)


    def get_detail_url(self, source):
        """获取详情页的url"""
        detail_urls = re.findall('<a class="position_link" href="(.*?)"', source)
        for detail_url in detail_urls:
            # print(detail_url)
            # 显式等待
            # element = WebDriverWait(self.driver, timeout=10).until(
            #     EC.presence_of_element_located((By.CLASS_NAME, "list_item_top"))
            # )
            self.get_info(detail_url)
            time.sleep(1)
            # return


    def get_info(self, detail_url):
        self.driver.execute_script("window.open('{}')".format(detail_url))
        self.driver.switch_to.window(self.driver.window_handles[1])

        xpath_str = "/html/body/div[2]/div/div[1]/dd/p[1]"
        # 职位名称
        position_name = self.driver.find_element_by_class_name('name').text
        # 薪水
        salary = self.driver.find_element_by_xpath(xpath_str+"/span[1]").text
        re_str = re.compile("[\s/]")
        # 所在城市
        city = self.driver.find_element_by_xpath(xpath_str+"/span[2]").text
        city = re.sub(re_str, "", city)
        # 工作经验
        experience = self.driver.find_element_by_xpath(xpath_str+"/span[3]").text
        experience = re.sub(re_str, "", experience)
        # 学历要求
        educate = self.driver.find_element_by_xpath(xpath_str+"/span[4]").text
        educate = re.sub(re_str, "", educate)
        # 公司
        company_name = self.driver.find_element_by_class_name("fl-cn").text.strip()
        # 发布时间
        release_time = self.driver.find_element_by_class_name("publish_time").text.split(" ")[0]
        # if len(release_time) <= 5:
        #     if "天前" in release_time:
        #
        #     release_time = time.strftime("%Y-%m-%d", time.localtime())

        print(position_name, salary, city, experience, educate, release_time, company_name + "(公司)")
        # 职位描述
        describe_0 = self.driver.find_element_by_class_name("job-advantage").text
        describe_1 = self.driver.find_element_by_class_name("job_bt").text
        describe_2 = self.driver.find_element_by_class_name("work_addr").text

        describe = describe_0 + describe_1 + describe_2

        # print(describe_0)
        # print(describe_1)
        # print(describe_2)
        print(describe)

        # 关闭当前页面
        self.driver.close()

        self.driver.switch_to.window(self.driver.window_handles[0])




if __name__ == '__main__':
    lagou = LaGou()
    lagou.get_page()

