#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-08-26  15:50

import requests
from bs4 import BeautifulSoup
# 导入可视化模块
from pyecharts import Bar

"""
    当爬取港澳台的天气时，由于html代码不规范，table标签只有开始标签没有结束标签
    lxml解析器不能解析，所以用容错性更强的html5lib解析器
"""


ALL_WETHER = []


def spider():

    urls = [
        "http://www.weather.com.cn/textFC/hb.shtml",
        "http://www.weather.com.cn/textFC/db.shtml",
        "http://www.weather.com.cn/textFC/hd.shtml",
        "http://www.weather.com.cn/textFC/hz.shtml",
        "http://www.weather.com.cn/textFC/hn.shtml",
        "http://www.weather.com.cn/textFC/xb.shtml",
        "http://www.weather.com.cn/textFC/xn.shtml",
        "http://www.weather.com.cn/textFC/gat.shtml"
    ]

    print("{:<10}   {:<10}".format("- 城市 -", "- 最低温度 -"))

    # 页面解析
    for url in urls:
        parse(url)

    # print(ALL_WETHER)

    # for wether in ALL_WETHER:
    #     min_temperature = wether.get("min_temperature")
    #     print(min_temperature)
    ALL_WETHER.sort(key=lambda wether: wether.get("min_temperature"))
    # print(ALL_WETHER)

    # 数据可视化
    visualization(ALL_WETHER)


def parse(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    response.encoding = "utf-8"
    content = response.text

    """使用容错性更强的html5lib解析器"""
    # soup = BeautifulSoup(content, "lxml")
    soup = BeautifulSoup(content, "html5lib")
    conMidtab = soup.find('div', class_="conMidtab")
    tables = conMidtab.find_all("table")
    for table in tables:
        trs = table.find_all("tr")[2:]
        for index,tr in enumerate(trs):
            tds = tr.find_all('td')
            # city_td = tds[0]
            if index == 0:
                city_td = tds[1]
                # province = tds[0]
                province = list(tds[0].stripped_strings)[0]
                # print(province)
            else:
                city_td = tds[0]

            city = list(city_td.stripped_strings)[0]
            city = province+" - "+city
            min_temperature = list(tds[-2].stripped_strings)[0]

            print("{:^7}      {:^10}".format(city, min_temperature))

            ALL_WETHER.append({'city': city, "min_temperature": int(min_temperature)})

        print("="*25)


def visualization(ALL_WETHER):
    """数据可视化"""
    ALL_WETHER = ALL_WETHER[0:20]
    cities = map(lambda data: data.get("city"), ALL_WETHER)
    temperature = map(lambda data: data.get("min_temperature"), ALL_WETHER)

    echart = Bar("中国天气排行榜Top20")
    echart.add("", list(cities), list(temperature))     # city为横坐标，temperature为纵坐标
    echart.render("中国天气排行榜Top20.html")   # 渲染到网页


if __name__ == '__main__':
    spider()