#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-08-22  14:04

from lxml import etree

"""
任务：
    以拉勾网的招聘信息为例（信息见/New_Folder/Lagou.html）：
    1、获取所有的h3标签
    2、获取第二个h3标签
    3、获取所有class为add的span标签
    4、获取拥有href的a标签
    5、获取a标签中href的属性
    6、获取所有的纯文本信息+链接
    
语法：
    获取href属性：/@href； 如：//a/@href    获取所有a标签的href属性，
                            区别于//a[@href]  获取有href属性的a标签
                            
    获取文本：/text()    如：//a/text()    获取所有a标签的文本 
    
    在某一个标签下，再一次执行xpath语句，进一步提取数据时，
        可使用“.”代表当前已经执行xpath的标签（具体实现在任务6）

【Tip】：
    1、Element对象执行xpath语句，返回的是list
    2、使用xpath获取标签时，返回的是_Element对象
        获取具体属性时，返回的是str字符串
"""

file = "New_Folder/Lagou.html"

# 构建parser
parser = etree.HTMLParser(encoding="utf-8")
# 解析html
html = etree.parse(file, parser=parser)

# 1、获取所有的h3标签
# h3s = html.xpath("//h3")
# for h3 in h3s:
#     print(etree.tostring(h3, encoding="utf-8").decode("utf-8"))

# 2、获取第二个li标签
# h3 = html.xpath("//li[2]")[0]
# print(etree.tostring(h3, encoding='utf-8').decode("utf-8"))


# 3、获取所有class为add的span标签
# spans = html.xpath("//span[@class='add']")
#
# for span in spans:
#     print(etree.tostring(span, encoding="utf-8").decode("utf-8"))

# 4、获取拥有href的a标签
# aList = html.xpath("//a[@href]")
# for a in aList:
#     print(etree.tostring(a, encoding="utf-8").decode("utf-8"))

# 5、获取a标签中href的属性
# hrefs = html.xpath("//a/@href")
#
# for href in hrefs:
#     print(href)


# 6、获取所有的纯文本信息+链接
lis = html.xpath("//li")
# print(lis)

list = []

for li in lis:
    # print(etree.tostring(li, encoding="utf-8").decode("utf-8"))

    """进一步提取数据"""

    # 获取链接
    a = li.xpath(".//a[@data-lg-tj-id='8E00']/@href")[0]
    # 获取标题
    h3 = li.xpath(".//h3/text()")[0]
    # 获取地点
    add = li.xpath(".//span[@class='add']/em/text()")[0]
    # 获取发布时间
    format_time = li.xpath(".//span[@class='format-time']/text()")[0]
    # 获取薪资
    money = li.xpath(".//span[@class='money']/text()")[0]
    # 获取工作经验
    experience = li.xpath(".//div[@class='li_b_l']/text()")
    finalExperience = ""
    i = 0
    for e in experience:
        finalExperience += e

    finalExperience = finalExperience.strip()
    # 获取公司名
    company = li.xpath('.//div[@class="company_name"]/a/text()')[0]
    # 获取融资
    industry = li.xpath('.//div[@class="industry"]/text()')[0].strip()
    # 获取待遇
    treatment = li.xpath('.//div[@class="li_b_r"]/text()')[0].strip("“”")

    dict = {
        "Url": a,
        "Position": h3,
        "Address": add,
        "Money": money,
        "treatment": treatment,
        "Experience": finalExperience,
        "company": company,
        "industry": industry,
        "Format_time": format_time
    }

    list.append(dict)

for i in list:
    print(i)