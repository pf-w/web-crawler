# -*- coding: utf-8 -*-
import scrapy
from Spider_study.Scrapy_study.qsbk_scrapy.qsbk_scrapy.items import QsbkScrapyItem
from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import SelectorList

"""
本文件是自己创建的爬虫文件，使用的是传统的爬虫
"""


class QsbkSpider(scrapy.Spider):    # 必须要继承scrapy.Spider_study

    # 爬虫名，运行爬虫都是根据这个名字来运行的，若一个项目中有多个爬虫，要注意名字唯一
    name = 'qsbk'

    # 允许的域名，不会访问到其他的域名上
    allowed_domains = ['qiushibaike.com']

    # 开始的url，也可以有多个, 一般为一个
    # start_urls = ['http://qiushibaike.com/']
    # 将开始url修改为自己需要的页面
    start_urls = ['https://www.qiushibaike.com/text/page/1/']

    basic_domain = 'https://www.qiushibaike.com'

    def parse(self, response):
        """
        response: 是由Spider通过start_urls开始把request发送给Engine，
        Engine发送给scheduleer进行调度, 然后再通过Engine把request发送给Downloader，
        返回的response通过Engine返回给Spider，即参数response
        """
        # print("="*50)
        # print(type(response))   # HtmlResponse对象
        # print("="*50)

        # SelectorList
        divs = response.xpath('//div[@id="content-left"]/div')
        # print("###")
        # print(type(divs))   # SelectorList
        # print("###")

        for div in divs:
            # print(type(div))    # Selector
            author = div.xpath(".//h2/text()").get().strip()    # get()相当于extract_first()提取第一个，并把Selector转换成str
            text = div.xpath(".//div[@class='content']//text()").getall()  # getall()相当于extract()提取所有信息，返回list，其中每个都是str
            text = text[1].strip()

            # duanzi = {"author": author, "text": text}
            # yield duanzi

            # 先把items中的QsbkScrapyItem导入进来
            duanzi = QsbkScrapyItem(author=author, text=text)
            # duanzi = QsbkScrapyItem({'author': author, 'text': text})
            yield duanzi

        # 实现翻页
        next_url = response.xpath('//ul[@class="pagination"]/li[last()]/a/@href').get()

        if not next_url:
            return  # href如果不存在，就表示是最后一页，直接退出函数
        else:   # 若果href存在，则再发送另一个请求
            # next_url = "/text/page/13/"
            yield scrapy.Request(url=QsbkSpider.basic_domain + next_url, callback=self.parse)  # 发送请求
            # url是要请求哪个url，callback是请求回来要执行那个函数，还是执行self.parse()进行下一页的页面解析
