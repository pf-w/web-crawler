#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2019-04-09  17:11

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, re


class PurchaseTickets(object):
    url = "https://www.12306.cn/index/"

    def __init__(self):
        self.from_station = input("出发地：")
        self.to_station = input("目的地：")
        self.train_date = input("出发日期【如:2019-04-08】：")
        self.student = input("是否购买学生票【Y/N】：")
        # self.g_d = input("是否只选择高铁/动车【Y/N】：")
        self.url = PurchaseTickets.url
        self.driver = webdriver.Chrome()

    def run(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.search_tickets()

    def search_tickets(self):
        # 显式等待页面加载完成
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "fromStationText"))
        )

        time.sleep(2)
        other = self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/ul/li[1]/a')
        other.click()

        # 输入并选择出发地
        from_station_text = self.driver.find_element_by_id('fromStationText')
        from_station_text.click()
        from_station_text.clear()
        from_station_text.send_keys(self.from_station)

        try:
            from_station_list = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//div[@id="panel_cities"]//span[text()="{}"]'.format(self.from_station)))
            )
            from_station_list.click()
        except:
            print("无法匹配到出发地")

        # 输入并选择目的地
        to_station_text = self.driver.find_element_by_id('toStationText')
        to_station_text.clear()
        to_station_text.send_keys(self.to_station)
        try:
            to_station_list = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//div[@id="panel_cities"]//span[text()="{}"]'.format(self.to_station)))
            )
            to_station_list.click()
        except:
            print("无法匹配到目的地")

        # 学生票
        if self.student.upper() == "Y":
            stu_checkBox = self.driver.find_element_by_id('isStudentDan')

            if stu_checkBox.get_attribute("class") != "disabled":
                stu_checkBox.click()
            else:
                print("========================")
                print("     学生票暂时无法购买    ")
                print("========================")

        # 高铁动车
        # if self.g_d.upper() == "Y":
        #     self.driver.find_element_by_id('isHighDan').click()
        self.driver.find_element_by_id('isHighDan').click()     # 默认高铁动车

        # 点击查询
        self.driver.find_element_by_id('search_one').click()
        # time.sleep(2)
        self.choose_tickets()

    def choose_tickets(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        current_url = self.driver.current_url

        # 修改url中的日期
        if self.train_date != time.strftime("%Y-%m-%d"):
            url = re.sub('&date=(.*?)&', "&date={}&".format(self.train_date), current_url)
            self.driver.get(url)
            # print(url)

        # 列车信息
        # list_title = self.driver.find_element_by_id('float').text.split()
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//tbody[@id='queryLeftTable']/tr"))
            )
        except:
            print("无法获取车次")
        train_infos = self.driver.find_elements_by_xpath('//tbody[@id="queryLeftTable"]//tr[not(@datatran)]')   # 没有datatran属性的tr标签

        train_ids = {}
        for train_info in train_infos:
            # 获取车次ID
            train_id = train_info.get_attribute("id")
            # 获取train的number下标
            train_num_index = re.finditer("[A-Z]", train_id[:-2])
            for i in train_num_index:
                train_num_index = i.span()[0]
            # 获取train的number
            train_num = train_id[train_num_index:-2]
            # 放入字典
            train_ids[train_num] = train_id
            # print(train_num + "---" + train_id)

        while True:
            train_num = input("\n选择车次,(输入 q 退出)：").upper()

            if train_num.lower() == 'q':
                return

            train_num_id = train_ids.get(train_num)

            time.sleep(1)
            try:
                # 默认是选择二等座
                sec_chair = self.driver.find_element_by_xpath('//*[@id="{}"]/td[4]'.format(train_num_id)).text
                if sec_chair != "无":
                    buy_button = self.driver.find_element_by_xpath('//*[@id="{}"]/td[13]/a'.format(train_num_id))
                    buy_button.click()
                    print("------------------------")
                    print("      请在浏览器中登录     ")
                    print("------------------------")
                    break
                else:
                    print("改车次暂无余票(二等座)！")
            except:
                print("【车次输入有误！！！】")

        # 循环等待跳转
        while True:
                if self.driver.current_url == "https://kyfw.12306.cn/otn/confirmPassenger/initDc":
                    self.choose_seat()
                    break

    def choose_seat(self):
        print(self.driver.current_url)

        # time.sleep(1)

        print("------------------------")
        print("      请核对以下信息      ")
        print("------------------------")
        sub_button = WebDriverWait(self.driver, 1000).until(
            EC.presence_of_element_located((By.ID, "submitOrder_id"))
        )
        ticket_info = self.driver.find_element_by_xpath('//*[@id="ticket_tit_id"]').text
        print(ticket_info + "\n")

        # 获取乘车人列表
        user_list = self.driver.find_elements_by_xpath('//*[@id="normal_passenger_id"]//li/label')

        for i, user in enumerate(user_list):
            print(str(i) + " - " + user.text)

        i = input("请选择乘车人（序号）：")
        # user_checkbox = self.driver.find_element_by_id('normalPassenger_{}'.format(int(i)-1))
        # user_checkbox = self.driver.find_element_by_xpath('//*[@id="normalPassenger_{}"]'.format(int(i)-1))
        user_checkbox = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, 'normalPassenger_{}'.format(int(i))))
        )
        user_checkbox.click()

        # 判断元素是否显示，是否弹出小窗口，并关闭
        if self.driver.find_element_by_id('qd_closeDefaultWarningWindowDialog_id').is_displayed():
            tip = self.driver.find_element_by_id('content_defaultwarningAlert_hearder').text
            print("\n【Tip:】\n" + tip)
            self.driver.find_element_by_id('qd_closeDefaultWarningWindowDialog_id').click()

        # 获取票信息，并打印
        ticket_type = self.driver.find_element_by_xpath('//*[@id="ticketType_1"]/option[1]').text
        chair_type = self.driver.find_element_by_xpath('//*[@id="seatType_1"]/option[1]').text.split()
        user_name = self.driver.find_element_by_id("passenger_name_1")
        user_name = user_name.get_attribute('value')
        certificate_type = self.driver.find_element_by_xpath('//*[@id="passenger_id_type_1"]/option[1]').text
        card_ID = self.driver.find_element_by_id('passenger_id_no_1')
        card_ID = card_ID.get_attribute('value')
        phone = self.driver.find_element_by_id('phone_no_1')
        phone = phone.get_attribute('value')

        print("\n乘车人信息：")
        print(ticket_type)
        print(chair_type[0])
        print(user_name)
        print(certificate_type.strip())
        print(card_ID)
        print(phone + "\n")

        sub_verification = input("输入 Y 提交：")
        if sub_verification.upper() == 'Y':
            sub_button.click()

        # 提交窗口
        # self.driver.find_element_by_id('content_checkticketinfo_id')
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, 'content_checkticketinfo_id'))
        )
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, 'erdeng1'))
        )

        # time.sleep(1)

        # 获取选座信息
        a_seat = self.driver.find_element_by_id('1A')
        b_seat = self.driver.find_element_by_id('1B')
        c_seat = self.driver.find_element_by_id('1C')
        d_seat = self.driver.find_element_by_id('1D')
        f_seat = self.driver.find_element_by_id('1F')

        print("————————————————————————————————————————————")
        print(" 窗 |   A   B   C   | 过 道 |   D   F   | 窗 ")
        print("————————————————————————————————————————————")



        t = "已经选好座啦"
        while True:
            choose_seat = input("选座啦！！！ (≧∀≦)").upper()
            if choose_seat == 'A':
                try:
                    a_seat.click()
                    break
                except:
                    continue
            elif choose_seat == 'B':
                try:
                    b_seat.click()
                    break
                except:
                    continue
            elif choose_seat == 'C':
                try:
                    c_seat.click()
                    break
                except:
                    continue
            elif choose_seat == 'D':
                try:
                    d_seat.click()
                    break
                except:
                    continue
            elif choose_seat == 'F':
                try:
                    f_seat.click()
                    break
                except:
                    continue
            else:
                t = "已跳过选座"
                print(t)
                break
        # 余票信息
        text = self.driver.find_element_by_id('sy_ticket_num_id').text
        print(t + text)

        # 点击确认
        self.driver.find_element_by_id('qr_submit_id').click()
    #     https://kyfw.12306.cn/otn//payOrder/init?random=1554898278841
        while True:
            if "https://kyfw.12306.cn/otn//payOrder/init" in self.driver.current_url:
                self.pay_tickets()
                break

    def pay_tickets(self):
        # self.driver.find_element_by_id('ins_f_close').click()
        try:
            WebDriverWait(self.driver, 120).until(
                EC.presence_of_element_located((By.ID, "payButton"))
            ).click()
        except:
            pass
        print("------------------------")
        print("      在浏览器中完成支付")
        print("------------------------")


if __name__ == '__main__':
    print("------------------------")
    print("    默认高铁/动车二等座    ")
    print("------------------------")

    pt = PurchaseTickets()
    pt.run()

