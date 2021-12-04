import scrapy
from selenium import webdriver

class KuwoSpider(scrapy.Spider):
    name = 'kuwo'
    # allowed_domains = ['www.kuwo.cn']
    start_urls = ['https://www.kuwo.cn/search/list?key=%E5%91%A8%E6%9D%B0%E4%BC%A6']

    def __init__(self):
        self.bro = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")

    def parse(self, response):
        li_list =  response.xpath('//*[@id="__layout"]/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/ul/li')
        for li in li_list:
            img_cover = li.xpath('./div[1]/img[1]/@data-src').extract_first()
            name = li.xpath('./div[2]/a[1]/text()').extract_first()
            artist = li.xpath('./div[3]/span[1]/text()').extract_first()
            album =  li.xpath('./div[4]/span[1]/text()').extract_first()
            time =   li.xpath('./div[5]/span[1]/text()').extract_first()

            song = {
                'img_cover':img_cover,
                'name' : name,
                'artist':artist,
                'album':album,
                'time': time
            }
            print(song)
        pass

    def close(spider, reason):
        spider.bro.close()
