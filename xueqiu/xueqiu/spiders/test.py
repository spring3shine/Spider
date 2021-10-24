import os

import scrapy
from scrapy.http import HtmlResponse


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['https://xueqiu.com']
    start_urls = ['https://xueqiu.com/S/SH600996']

    def parse(self, response: HtmlResponse):
        print(os.listdir())
        print(response.status)
        with open('./files/response.html','w',encoding='utf-8') as f:
            f.write(response.text)


        with open('./files/stock_SH600996.txt','w',encoding='utf-8') as f:
            f.write(response.xpath('/html/body/script[contains(text(),\'STOCK_PAGE\')]/text()').get())
        pass
