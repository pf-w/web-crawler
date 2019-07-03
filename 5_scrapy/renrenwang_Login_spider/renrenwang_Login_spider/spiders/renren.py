# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    # def parse(self, response):
    #     pass

    # 爬虫一开始就使用POST请求需要重写start_request（）
    def start_requests(self):
        url = "http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2019341735720"

        data = {
            "email": "17866673602",
            "password": "A1011467276"
        }

        yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse_page)

    def parse_page(self, response):

        with open("renren.html", 'w', encoding='utf-8') as fp:
            fp.write(response.text)
