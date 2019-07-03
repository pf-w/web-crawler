import os, sys
from selenium import webdriver
import datetime
import time
from os import path

'''
    
'''

#driver = webdriver.Chrome()
driver = webdriver.Edge()
driver.maximize_window()

def login():
    # 打开淘宝登录页，并进行扫码登录
    #driver.get("https://www.taobao.com/")
    
    time.sleep(1)

    login_button = driver.find_element_by_link_text("亲，请登录")
    
    if login_button:
        login_button.click()
        print("\n\n=================================================")
        print("请在15秒内完成扫码，若未完成请重新运行该脚本！！！")
        print("=================================================\n")

        #time.sleep(15)
        # 倒计时
        for i in range(15,-1,-1):
            print("\r请稍后:", i , " ", end="", flush=True)
            time.sleep(1)
        print("\n")
        
        driver.get("https://cart.taobao.com/cart.htm")
    time.sleep(1)

    # 点击购物车里全选按钮
    if driver.find_element_by_id("J_SelectAll1"):
        driver.find_element_by_id("J_SelectAll1").click()
        
    now = datetime.datetime.now()
    print('登陆成功：', now.strftime('%Y-%m-%d %H:%M:%S'))

def buy(buytime):
    
    while True:
        now =datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        
        # 对比时间，时间到的话就点击结算
        if now >= buytime:
            try:
                # 点击结算按钮
                if driver.find_element_by_id("J_Go"):
                   driver.find_element_by_id("J_Go").click()
                   driver.find_element_by_link_text('提交订单').click()
            except:
                time.sleep(0.1)
        print("\r当前时间：", now, "【若计时停止，按“回车”继续】", end="", flush=True)
        time.sleep(0.1)

if __name__ == "__main__":

    # 打开淘宝登录页，并进行扫码登录
    try:
        driver.get("https://www.taobao.com/")
    except Exception:
        print("请求出错，请检查网络！！！")
        
    while True:   
        times = input("请输入抢购时间：[ 时间格式‘2018-11-06 00:01:00.00’]\n")
        # 时间格式："2018-11-06 00:01:00.000000"
        
        times = times.replace("：", ":")     # 将用户输入的时间中的中文字符替换成英文字符

        print("输入的抢购时间为：", times, end="\n")

        verification = input("请确认抢购时间（Y(y)继续，N(n)重新输入）")

        if verification.upper() == "Y":
            break
    
    try:
        login()
        print("\n")
        buy(times)
    except Exception:
            print("\n未在规定时间内完成登陆，请重新运行！！！");
            
    
    
 
