# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Spider_study.Scrapy_study.qsbk_scrapy_crawlspider.qsbk_scrapy_crawlspider.items import QsbkScrapyCrawlspiderItem

class QsbkSpider(CrawlSpider):
    name = 'qsbk'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']

    rules = (
        Rule(LinkExtractor(allow=r'.+text/page/\d+/'), follow=True),
        Rule(LinkExtractor(allow=r'.+article/\d+'), callback='parse_item', follow=False),
    )

    # allowed_domains = ['kugou.com']
    # start_urls = ['https://www.kugou.com/yy/rank/home/1-6666.html?from=rank']
    # rules = [
    #     Rule(LinkExtractor(allow=r'.+/yy/rank/home/1-\d+\.html\?from=rank'), follow=True),
    #     Rule(LinkExtractor(allow=r'.+/song/v4uufcf.html'), follow=True),
    #     Rule(LinkExtractor(allow=r'.+?/[0-9a-zA-z/-]+?\.mp3'), callback='parse_item', follow=False),
    # ]

    def parse_item(self, response):
        item = {}
        item = QsbkScrapyCrawlspiderItem()
        item['title'] = response.xpath('//h1[@class="article-title"]/text()').get()
        item['author'] = response.xpath('//span[@class="side-user-name"]/text()').get()
        item['time'] = response.xpath('//span[@class="stats-time"]/text()').get()

        title = response.xpath('//h1[@class="article-title"]/text()').get()
        author = response.xpath('//span[@class="side-user-name"]/text()').get()
        time = response.xpath('//span[@class="stats-time"]/text()').get()
        print(author, time, title)

        item = QsbkScrapyCrawlspiderItem(title=title.strip(), author=author.strip(), time=time.strip())

        yield item

        # print(response)





