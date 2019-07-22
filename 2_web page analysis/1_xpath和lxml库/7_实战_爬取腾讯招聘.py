#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-08-24  9:22

"""
    腾讯招聘：
        第一页url: https://hr.tencent.com/position.php?&start=0
        第二页url: https://hr.tencent.com/position.php?&start=10
        第三页url: https://hr.tencent.com/position.php?&start=20

        使用的是Get请求，数据在页面中，不是Ajax异步加载
"""

import requests
from lxml import etree


DOMAIN = "https://hr.tencent.com/"

BASE_URL = "https://hr.tencent.com/position.php?&start={}0"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}

POSITION_INFO = {}

def get_page(pages_url):
    response = requests.get(pages_url, headers=HEADERS)
    # print(response.content.decode("utf-8"))
    content = response.content.decode("utf-8")
    # 解析  若解析的是文件，则使用etree.parse(file, parser)
    #       parse则用etree.HTMLParser(encodeing="")进行构造解析器
    html = etree.HTML(content)
    # page_info = html.xpath("//td[@class='l square']")
    page_info = html.xpath("//tr[@class='even'] | //tr[@class='odd']")

    detail_pages_url = []

    for i in page_info:
        detail_page_url = i.xpath(".//a/@href")[0]
        detail_page_url = DOMAIN + detail_page_url

        detail_pages_url.append(detail_page_url)

    return detail_pages_url


def get_detail_info(url):
    # print(url)

    response = requests.get(url, headers=HEADERS)
    content = response.content.decode('utf-8')

    html = etree.HTML(content)

    position = html.xpath("//td[@id='sharetitle']/text()")
    # print(position)

    info = html.xpath("//tr[@class='c bottomline']//td/text()")
    # print(info)

    POSITION_INFO["position"] = position
    POSITION_INFO["location"] = info[0]
    POSITION_INFO["type"] = info[1]
    POSITION_INFO["nums"] = info[-1]


    work_info = html.xpath("//ul[@class='squareli']")
    duties_info = work_info[0].xpath(".//li/text()")
    claim_info = work_info[1].xpath(".//li/text()")

    duties = ""
    for i in duties_info:
        duties += i
    claim = ""
    for i in claim_info:
        claim += i

    # print(duties)
    # print(claim)

    POSITION_INFO["duties"] = duties
    POSITION_INFO["claim"] = claim

    print(POSITION_INFO)


def spider():
    p = input("要爬取几页？")
    pages = [i for i in range(int(p))]
    for i in pages:
        pages_url = BASE_URL.format(i)
        # print(pages_url)
        detail_pages_url = get_page(pages_url)

        for url in detail_pages_url:
            get_detail_info(url)

    print("\n\n共计" + str(int(p)*10) + "条信息")

if __name__ == '__main__':
    spider()

