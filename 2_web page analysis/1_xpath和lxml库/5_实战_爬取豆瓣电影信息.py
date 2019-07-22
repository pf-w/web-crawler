#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-08-22  16:49

"""
    爬取豆瓣正在上映的电影
"""

import requests
from lxml import etree

url = "https://movie.douban.com/cinema/nowplaying/weifang/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Referer": "https://movie.douban.com/"
}

response = requests.get(url, headers=headers)
# print(response.content.decode("utf-8"))

# 将请求下来的数据放入变量或者写入文件（以放入变量为例）
# 对文件使用xpath时，要使用etree.parse(filr, parser)
content = response.content.decode("utf-8")

# 使用lxml对数据进行解析，以便使用xpath语句进行操作
html = etree.HTML(content)

# 进行提取数据
ul = html.xpath("//ul[@class='lists']")[0]
# print(ul)     # 第一个为正在上映 第二个为即将上映

# 进一步提取数据

lis = ul.xpath("./li")
# print(li)

movies = []

for li in lis:
    # 电影名
    title = li.xpath("@data-title")[0]
    # 评分
    score = li.xpath("@data-score")[0]
    # 上映时间
    date = li.xpath("@data-release")[0]
    # 地区
    region = li.xpath("@data-region")[0]
    # 导演
    director = li.xpath("@data-director")[0]
    # 演员
    actors = li.xpath("@data-actors")[0]
    # 海报
    poster = li.xpath(".//img/@src")[0]
    # 链接
    link = li.xpath(".//a['data-psource=poster']/@href")[0]

    # print(title, " " , score, " ", date, " ",
    #       region, " ", director, " ", actors, " ", poster, " ", link)

    movie = {
        "title": title,
        "score": score,
        "date": date,
        "region": region,
        "director": director,
        "actors": actors,
        "poster": poster,
        "link": link
    }

    movies.append(movie)

for movie in movies:
    print(movie)