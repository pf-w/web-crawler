#   !/usr/bin/env python3

#   -*- coding: utf-8 -*-

#   Created on 2018-08-26  11:32

"""
    【四种常见的对象】：
        1、Tag：BeautifulSoup中所有的标签多是Tag类型，BeautifulSoup的对象实质上也是
            Tag类型，所以一些方法比如：find、find_all...都是继承自Tag的方法

        2、BeautifulSoup：继承自Tag，用来生成BeautifulSoup树的，
            其中的find、find_all、select方法都是继承自Tag

        3、NavigableString：继承自Python中的str，使用方法和str一样

        4、Comment：继承自NavigableString, 代表注释的地方
            【注意】：string属性只能获取单行的文本，若文本有多行则获取不到
                    如：<p><!--注释--></p>  # 可以获取到文本<!--注释--> （单行）

                        # 不可以获取到（多行）
                       <p>
                            <!--注释-->
                       </p>


    【contents 和 children】：
        返回某个标签下的直接子元素，包括字符串；

        【区别】：contents返回的是list
                children返回的是iterator（迭代器）

"""

import __init__
from bs4 import BeautifulSoup

soup = BeautifulSoup(__init__.text, 'lxml')
print(type(soup))   # BeautifulSoup对象 继承自Tag

print('='*30)

tr = soup.find('tr')
print(type(tr))     # Tag对象

print('='*30)

div = soup.find('div')
text = div.string
print(type(text))   # NavigableString对象

print('='*30)

# p_1 = soup.find("p")
p_1 = soup.find_all("p",id="p_1")[0]
comment = p_1.string
print(type(comment))    # Comment对象
print(comment)


print("\n" + "#"*50, end="\n")

# 以div标签为例
contents = div.contents
print(contents)
print(type(contents))   # 返回list类型

print('='*30)

children = div.children
print(children)
print(type(children))   # 返回迭代器


