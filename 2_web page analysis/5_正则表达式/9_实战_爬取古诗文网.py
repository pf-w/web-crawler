#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-08-29  13:17

"""
    第一页：https://www.gushiwen.org/default_1.aspx
    第二页：https://www.gushiwen.org/default_2.aspx
    第三页：https://www.gushiwen.org/default_3.aspx

    使用get请求
"""

import __init__
import requests
import re


POETRY = []


def spider():
    url = "https://www.gushiwen.org/default_1.aspx"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    content = response.content.decode("utf-8")

    # print(content)

    # content = __init__.text     # 网络原因，暂用__init__中的text

    # print(content)
    parse(content)


def parse(content):
    """整篇古诗文"""
    # r = re.compile('<textarea.*?>(.*?)https.*?</textarea>', flags=re.DOTALL)
    # poetry = re.findall(r, content)    # re.DOTALL 表示"."能匹配\n
    # print(len(poetry))
    # for i in poetry:
    #     print(i)

    """标题"""
    title_r = re.compile('<div class="cont">.*?<b>(.*?)</b>', flags=re.DOTALL)
    titles = re.findall(title_r, content)

    """朝代 + 作者"""
    dynasty_author = re.findall('<p class="source"><a.*?>(.*?)</a>.*?<a.*?>(.*?)</a>', content, flags=re.DOTALL)

    """内容"""
    text = re.findall('<div class="contson".*?>(.*?)</div>', content, flags=re.DOTALL)

    for i in range(len(titles)):
        POETRY.append(
            {
                'title': titles[i],
                'dynasty': dynasty_author[i][0],
                'author': dynasty_author[i][1],
                # 'content': re.sub(" |<br>|\\n|<p>|</p>", "", text[i])
                'content': re.sub(" |<p>|</p>", "", text[i]).strip("\n")
            }
        )

    for i in POETRY:
        print(i)


if __name__ == '__main__':
    spider()