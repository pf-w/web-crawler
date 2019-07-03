
scrapy运行：

    1、在命令行中使用命令运行：

        进入项目的目录，执行scrapy crawl spider_name  【进入项目名，不是爬虫名】

    2、在项目中建立一个py文件，通过scrapy提供的命令行运行

        1、创建一个py文件

        2、导入scrapy中的cmdline

        3、执行命令：cmdline.execute("scrapy crawl spider_name".split())

                   cmdline.execute(["scrapy", "crawl", "spider_name"])

                   二者本质相同，都是用list
