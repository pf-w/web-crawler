# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonLinesItemExporter
import json

class QsbkScrapyCrawlspiderPipeline(object):
    def __init__(self):
        self.fp = open("qsbk.json", "wb")
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')

    def open_spider(self, spider):
        print("开始。。。")

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.fp.close()
        print("结束。。。")




import pymysql


# class QsbkScrapyCrawlspiderPipeline(object):
#     def __init__(self):
#         self.connect = pymysql.Connect(
#             host="localhost",
#             port=3306,
#             user="root",
#             password='root',
#             database="crawl"
#         )
#         self.cursor = self.connect.cursor()
#
#     def process_item(self, item, spider):
#         sql = "insert into qsbk(author,time,title) values (%s,%s, %s)"
#
#         author = item["author"].strip()
#         time = item['time'].strip()
#         title = item['title'].strip()
#
#         print(author, time, title)
#
#         self.cursor.execute(sql, (author, time, title))
#         self.connect.commit()
#
#     def close_spider(self, spider):
#         self.connect.close()
#         print("结束。。。")

