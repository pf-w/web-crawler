#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-08-23  13:07

"""
    爬取电影天堂的电影

"""

import requests
from lxml import etree

DOMAIN = "http://www.dytt8.net"

# "http://www.dytt8.net/html/gndy/dyzz/list_23_1.html"
base_url = "http://www.dytt8.net/html/gndy/dyzz/list_23_"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}


def get_url(pages):
    """返回页面url"""
    pages_url = []
    for i in range(len(pages)):
        page = base_url + str(i+1) + ".html"
        # print(page)
        pages_url.append(page)

    # print(pages_url)

    return pages_url


def spider_url(pages_url):
    """爬取详情页的url"""

    # print(pages_url)

    for i in pages_url:
        response = requests.get(i, headers=headers)

        # content = response.content.decode("utf-8")

        # response.encoding = "gbk"     # 编码并不影响提取的url
        content = response.text

        # print(content)
        html = etree.HTML(content)
        urls = html.xpath("//div[@class='co_content8']/ul//table//a/@href")
        if "/html/gndy/jddy/index.html" in urls:
            urls.remove("/html/gndy/jddy/index.html")
        # for url in urls:
        #     print(DOMAIN + url)


    return urls


def spider(urls):
    """获取详情页的信息"""
    movie = {}

    for url in urls:
        real_url = DOMAIN + url
        # print(real_url)
        response = requests.get(real_url, headers=headers)
        response.encoding = "gbk"
        content = response.text
        # print(content)
        html = etree.HTML(content)
        data = html.xpath("//div[@class='co_content8']//div[@id='Zoom']")[0]

        # print(data)

        infos = data.xpath(".//text()")

        # print(infos)

        for info in infos:
            if info.startswith("◎译　　名"):
                translated_name = info.replace("◎译　　名", "").strip()
                movie["translated_name"] = translated_name
            if info.startswith("◎片　　名"):
                name = info.replace("◎片　　名", "").strip()
                movie["name"] = name
            if info.startswith("◎年　　代"):
                year = info.replace("◎年　　代", "").strip()
                movie["year"] = year
            if info.startswith("◎产　　地"):
                location = info.replace("◎产　　地", "").strip()
                movie["location"] = location
            if info.startswith("◎类　　别"):
                movie_type = info.replace("◎类　　别", "").strip()
                movie["movie_type"] = movie_type
            if info.startswith("◎语　　言"):
                language = info.replace("◎语　　言", "").strip()
                movie["language"] = language
            if info.startswith("◎片　　长"):
                movie_size = info.replace("◎片　　长", "").strip()
                movie["movie_size"] = movie_size
            if info.startswith("ftp://"):
                thunderDownload = info.strip()
                movie["thunderDownload"] = thunderDownload

        # for i in movie.items():
        #     print(i)

        print(movie)

        # break


if __name__ == '__main__':

    end = input("要爬取几页？")

    pages = [p for p in range(1, int(end)+1)]

    # 返回page
    pages_url = get_url(pages)
    # print(pages_url)

    # 获取详情页的url
    detailsPage_url = spider_url(pages_url)
    # print(detailsPage_url)

    # 获取详情页的信息
    spider(detailsPage_url)

