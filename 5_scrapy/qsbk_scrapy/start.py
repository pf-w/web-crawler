#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2019-04-12  15:03

"""
此文件要在项目的直接子目录下
"""

from scrapy import cmdline

# 参数必须是list，其中元素是执行scrapy的命令
cmdline.execute(['scrapy', 'crawl', 'qsbk'])

