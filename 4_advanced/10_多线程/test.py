import os
import threading
import re
from queue import Queue
import requests
from urllib import request
from lxml import etree

# 定义一个全局变量，存储请求头headers数据
headers = {
    "User-Agent": "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"
}


class Producter(threading.Thread):
    """
    生产者模型：负责从起始url队列中提取url，进行解析，将得到的图片地址放入img图片队列中
    """

    def __init__(self, page_queue, img_queue, *args, **kwargs):
        # 改写父类threading.Thread的__init__方法，添加默认值
        super(Producter, self).__init__(*args, **kwargs)
        # 添加对象属性
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        """
        实现消费者模型的主要业务逻辑
        """
        while True:
            # 当请求队列为空，生产者停止生产
            if self.page_queue.empty():
                break
            # 获取起始url队列的对象，进行页面解析
            url = self.page_queue.get()
            self.parse_url(url)

    def parse_url(self, url):
        """
        实现解析指定页面的功能
        :param url: 传入待处理的页面url
        """
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
    """
    消费者模型的主要业务逻辑
    """

    def __init__(self, page_queue, img_queue, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        """
        实现读取图片url内容的功能
        """
        while True:
            if self.page_queue.empty() and self.img_queue.empty():
                break
            url, filename = self.img_queue.get()
            # urllib库里面的request模块可以读取图片url内容
            request.urlretrieve(url, "pic/" + filename)
            # 控制台输出提示信息
            print(filename + "-------下载完成！")


def main():
    # 创建page队列，存放请求的起始url;创建img队列，存放图片data的url
    page_queue = Queue(100)  # 设置队列的最大存储数量
    img_queue = Queue(1000)  # 设置队列的最大存储数量
    for i in range(100):
        start_url_format = "http://www.doutula.com/photo/list/?page={}".format(i)
        # print(start_url_format) #调试代码用
        page_queue.put(start_url_format)  # 将获取的起始url放入队列中
    # 生成多线程对象（多个生产者、消费者）。实现发送请求，获取响应，解析页面，获取数据
    for i in range(10):
        t = Producter(page_queue, img_queue)
        t.start()
    for i in range(10):
        t = Consumer(page_queue, img_queue)
        t.start()


if __name__ == '__main__':
    main()