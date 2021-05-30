import scrapy


class TextSpiderSpider(scrapy.Spider):
    name = 'text_spider'
    #allowed_domains = ['Scrapy.io']
    start_urls = ['https://python123.io/ws/demo.html']

    def parse(self, response):
        #从响应的url中提取名字，作为保存的文件名
        flname= response.url.split('/')[-1]
        with open(flname,'w')as f:
            f.write(response.body)
        self.log('Save file %s' %flname)

