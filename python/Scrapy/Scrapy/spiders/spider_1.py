import scrapy


class Spider1Spider(scrapy.Spider):
    name = 'spider_1'
    allowed_domains = ['Scrapy.io'] #域名
    start_urls = ['http://Scrapy.io/'] #这是list形式的

    def parse(self, response):   #解析页面的函数（bs4 正则 xpath）
        pass
