#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2019-03-27  14:31


import requests, time, re, os
from lxml import etree
import threading
from queue import Queue
from urllib import request

"""
    多线程下载表情包
"""

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"
}


class Producer(threading.Thread):
    """获取pic信息，并加入img队列"""
    def __init__(self,page_queue, img_queue, *args, **kwargs):  # 重写Thread中的__init__方法
        super(Producer, self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.page_queue.empty():     # 若page队列为空则结束
                break
            url = self.page_queue.get()  # 获取page
            self.get_pic(url)

    def get_pic(self, url):
        """获取pic信息"""
        # # url = "https://www.doutula.com/photo/list/?page=1"
        # html = requests.get(url=url, headers=headers)
        # elements = etree.HTML(html.text)
        # pics = elements.xpath('//div[@class="page-content text-center"]//img[@class="gif"]')
        # for i in pics:
        #     pic_url = i.xpath('.//@data-original')
        #     title = i.xpath('.//@alt')
        #
        #     if len(pic_url) == 0:
        #         continue
        #
        #     self.img_queue.put((pic_url, title))    # 加入img队列
        #
        #     time.sleep(1)

        response = requests.get(url=url, headers=headers)
        html = etree.HTML(response.text)
        # 使用lxml库里HTML解析器进行数据解析，利用xpath语法解析得到指定数据，返回一个element对象列表
        url_gifs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
        for url_gif in url_gifs:
            # element.get(属性名)可以获取属性值
            url_name = url_gif.get("alt")
            # 正则表达式替换非法字符
            url_name = re.sub(r"[\!！\.\?？，]", "", url_name).strip()
            url_link = url_gif.get("data-original")
            # os模块中os.path.splitext()可以获取url的后缀名
            url_suffix = os.path.splitext(url_link)[1]
            filename = url_name + url_suffix
            # 队列的put（）里面传的是元组或者列表
            self.img_queue.put((url_link, filename))


class Consumer(threading.Thread):
    def __init__(self,page_queue, img_queue, *args, **kwargs):
        super(Consumer, self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            # 若img队列中没有图片信息，并且page队列为空，则结束
            self.download()
            if self.img_queue.empty() and self.page_queue.empty():
                break

    def download(self):
        # url, title = self.img_queue.get()
        url, filename = self.img_queue.get()
        # pic_url = url[0].split("!")[0]
        #
        # filename = title[0] + "." + pic_url.split(".")[-1]
        # print(filename)

        print("\n正在下载 >>> {}".format(url))
        pic = requests.get(url=url.strip(), headers=headers)
        with open(r"pic\{}".format(filename), "wb") as fp:
            fp.write(pic.content)
        # request.urlretrieve(url=pic_url, filename="pic/{}".format(filename))
        print("\n下载完成 <<< %s" % url)


def multi_threading():
    page_queue = Queue(100)
    img_queue = Queue(1000)

    page = int(input("爬取几页？"))
    for i in range(page):
        url = "https://www.doutula.com/photo/list/?page={}".format(i)
        print(url)
        page_queue.put(url) # 将page_url放入page队列

    for i in range(5):
        t = Producer(page_queue, img_queue)
        t.start()
    for i in range(5):
        t = Consumer(page_queue, img_queue)
        t.start()


if __name__ == '__main__':
    multi_threading()












