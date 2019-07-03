#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-08-24  14:00

"""
    使用BeautifulSoup提取信息

    使用find() 或 find_all()进行提取数据

"""
import __init__
from bs4 import BeautifulSoup

"""
    任务：
        1、获取所有的tr标签
        2、获取第二个tr标签
        3、获取所有class为even的tr标签
        4、获取id为test、class也为test的a标签
        5、获取所有a标签的href属性（2种方法）
        6、获取所有的文本信息
        
    【注意】：
        1、find()和find_all()的参数：
            两者参数一致，（区别见2）， 以find_all（）为例：
            find_all(Tag, limit, attrs):
                Tag: 是要提取的标签; 如：find_all("a")   提取所有的a标签
                limit：限制要提取的个数，
                    如：find_all("a", limit=2) 只提取前两个a标签
                attrs: 以dict的形式传入过滤条件； 
                    如: find_all('a', attrs={"class": 'test'})   提取class为test的a标签
                    如：find_all('a', sttrs={"class": 'test', "id": 'abc'})   提取class为test并且id为test的a标签
                    
            【注意】：
                attrs属性可以被关键字参数(标签的具体属性)代替，
                如：find_all('a', class_="test")  “class”与python中的关键字冲突，所以后面有一个“_”
                如：find_all('a', class_="test", id="test")   提取class为test并且id为test的a标签
                         
        2、find()和find_all()的区别：
            find只返回第一个匹配到的标签
            find_all()返回所有匹配到的标签，以list形式返回
            
        3、BeautifulSoup中find_all()不能像xpath那样直接找到，而是一层一层的找
            如：提取a标签的href属性，xpath("//a/@href")就可以找到a的href属性，
                而find_all()首先要找到所有的a标签，再找到a标签的href属性
                
        4、获取文本：
            string属性、strings属性、stripped_strings属性、get_text()方法
            
            1、string属性：获取当前标签的文本，不能获取子孙标签的文本, 文本若有多行则获取不到
                如：soup.find('td').string 获取td的文本，不能获取子孙标签的文本

            2、strings属性: 获取当前标签或子孙标签的文本，
                返回一个生成器，可用for循环遍历, 包含空的字符串
                
            3、stripped_strings属性：获取标签的文本或子孙标签的文本，
                返回一个生成器，不包含空字符串
            
            4、get_text()方法：获取当前标签或子孙标签的文本，返回字符串, 包含空字符串
"""

soup = BeautifulSoup(__init__.text, "lxml")

# 1、获取所有的tr标签
# trs = soup.find_all("tr")
# for tr in trs:
#     print(tr)
#     print("="*50)   # 分隔开


# 2、获取第二个tr标签
# tr = soup.find_all('tr', limit=2)[1]    # find_all()buneng像xpath语句一样,只能通过返回列表的下标取到
# print(tr)

# 2.2 获取除第一个外所有的tr标签
# trs = soup.find_all('tr')[1:]
# for tr in trs:
#     print(tr)
#     print("="*50)


# 3、获取所有class为even的tr标签
"""方法一"""
# trs = soup.find_all('tr', attrs={"class": "even"})
"""方法二"""
# trs = soup.find_all('tr', class_='even')
# for tr in trs:
#     print(tr)
#     print("="*50)


# 4、获取id为test、class也为test的a标签
# aList = soup.find_all('a', class_="test", id="test")
# for a in aList:
#     print(a)
#     print('='*50)


# 5、获取所有a标签的href属性 （2种方法）
# aList = soup.find_all('a')
# for a in aList:
#     """方法一"""
#     # href = a['href']
#     """方法二"""
#     href = a.attrs["href"]
#     print(href)
#     print('='*50)


# 6、获取所有的文本信息（逐层递进）
# 分析：
#   1、若直接获取td，则td下a标签的内容则获取不到
#   2、先获取tr，
#   3、由于第一个tr是标题(无用信息)，则从第二个开始
trs = soup.find_all('tr')[1:]
# print(type(trs))  # List
for tr in trs:
    # print(type(tr))   # Tag
    tds = tr.find_all("td")
    # print(type(tds))  # list

    """方法一(string)"""
    # title = tds[0].find('a').string
    # type = tds[1].string
    # nums = tds[2].string
    # location = tds[3].string
    # submit_date = tds[4].string
    # print(title, " ", type, " ", nums, " ", location, " ", submit_date)

    """方法二(strings)"""
    # textGenerator = tr.strings   # 提取当前标签或子孙标签的文本，返回生成器，包含空字符串
    # textList = list(textGenerator)
    # print(textList)
    # # for text in textList:
    # #     print(text)
    # #     print("="*50)

    """方法三(stripped_strings)"""
    # textGenerator = tr.stripped_strings  # 提取当前标签或子孙标签的文本，返回生成器，不包含空字符串
    # # print(text)
    # textList = list(textGenerator)
    # print(textList)

    """方法四(get_text)"""
    # 获取当前标签的文本
    # type = tds[1].get_text()
    # print(type)

    # 获取子孙标签的文本
    text = tr.get_text()
    print(text)     # str类型

