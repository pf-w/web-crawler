

创建scrapy项目后，先修改以下两个设置：

    1、修改遵守robots协议：
        ROBOTSTXT_OBEY = False  # 默认为True

        如果遵守robots协议，在爬取之前要在网站的根目录中查找robots.txt文件
        若果没有robots.txt文件就会返回，不会爬取到任何数据

    2、在DEFAULT_REQUEST_HEADERS = {}中添加'User-Agent'

        【是在后面添加，不是将原本有的删除】
