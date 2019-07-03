# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
"""
    保存成Json的第一种方法
"""
# class QsbkScrapyPipeline(object):
#     def __init__(self):
#         self.fp = open('duanzi.json', 'w', encoding='utf-8')
#
#     def open_spider(self, spider):
#         print("爬虫开始了。。。")
#
#     def process_item(self, item, spider):
#         """
#         将数据保存到json文件中
#         item: 若spider中通过yield返回数据，则被参数item接收
#         """
#         json_str = json.dumps(dict(item), ensure_ascii=False)   # 使用items定义模型后是QsbkScrapyItem对象，必须转换成dict后才能使用dunps
#         self.fp.write(json_str + "\n")
#         return item
#
#     def close_spider(self, spider):
#         self.fp.close()
#         print("爬虫结束了。。。")

"""
    保存成Json的第二种方法
"""
# from scrapy.exporters import JsonItemExporter
# class QsbkScrapyPipeline(object):
#     def __init__(self):
#         self.fp = open('duanzi_1.json', 'wb')
#         self.exporter = JsonItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')
#         self.exporter.start_exporting()
#
#     def open_spider(self, spider):
#         print("爬虫开始了。。。")
#
#     def process_item(self, item, spider):
#         """
#         将数据保存到json文件中
#         item: 若spider中通过yield返回数据，则被参数item接收
#         """
#         self.exporter.export_item(item)
#         return item
#
#     def close_spider(self, spider):
#         self.exporter.finish_exporting()
#         self.fp.close()
#         print("爬虫结束了。。。")


"""
    保存成Json的第三种方法
"""
from scrapy.exporters import JsonLinesItemExporter  # exporter 出口
class QsbkScrapyPipeline(object):
    def __init__(self):
        self.fp = open('duanzi_2.json', 'wb')
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')

    def open_spider(self, spider):
        print("爬虫开始了。。。")

    def process_item(self, item, spider):
        """
        将数据保存到json文件中
        item: 若spider中通过yield返回数据，则被参数item接收
        """
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.fp.close()
        print("爬虫结束了。。。")
