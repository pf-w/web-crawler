

在pycharm中无法直接将建scrapy项目，只能在shell中使用命令创建

    命令：

        scrapy startproject [项目名]

    执行命令后会自动生成以下目录：

        scrapy项目目录：
            ## 项目名
            |  == 这个名字跟上面一样
            |  |  -- spider  【在这里写爬虫，对应scrapy架构图中的Spider】
            |  |  |  - __init__.py
            |  |  |  - XXX.py   【XXX为爬虫名，运行时要用，所以要唯一】
            |  |
            |  |  -- items.py   【定义要爬取数据的模型，对应item pipelines】
            |  |
            |  |  -- middleware.py  【把下载器中间件和爬虫中间件放到此文件，对应下载中间件和爬虫中间件】
            |  |
            |  |  -- pipelines.py   【处理爬取下来的数据，对应item pipelines】
            |  |
            |  |  -- settings.py    【本爬虫的配置信息，如：设置headers、ip代理池、延迟等】
            |
            |  == scrapy.cfg    【项目的配置文件】

    创建完项目后，还需要创建爬虫，还是用命令创建：【需要进入工程目录】
        1、进入工程目录

        2、执行命令：scrapy genspider spider_name "domain"

            scrapy genspider 爬虫名 "域名"       如： scrapy genspider qsbk_spider "qiushibaike.com"

            genspider：其中gen表示generate：生成、spider ：蜘蛛


    【综上】：创建scrapy项目（只能通过命令创建）：

        1、进入要创建项目的目录

        2、创建项目：scrapy startproject 项目名

        3、进入项目目录

        4、创建爬虫：scrapy genspider 爬虫名 "域名"
