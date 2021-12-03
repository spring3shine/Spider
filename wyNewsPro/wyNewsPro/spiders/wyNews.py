import scrapy
from selenium import webdriver

class WynewsSpider(scrapy.Spider):
    name = 'wyNews'
    # allowed_domains = ['https://news.163.com/']
    start_urls = ['https://news.163.com//']


    model_urls = []

    def __init__(self):
        self.bro = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")

    def parse(self, response):
        lis = response.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul//li')
        model_list = {2: '国内', 3: '国际', 5: '军事', 6: '航空'}
        for pos in model_list.keys():
            name = lis[pos].xpath('./a/text()').extract_first()
            href = lis[pos].xpath('./a/@href').extract_first()
            print(name, href)
            self.model_urls.append(href)

        for url in self.model_urls:
            yield scrapy.Request(url, callback=self.parse_model)

    def parse_model(self, response):
        news_list = response.xpath('/html/body/div[1]/div[3]/div[4]/div[1]/div[1]/div/ul/li/div/div')
        for news in news_list:
            img_url = news.xpath('./a/@href').extract_first()
            title = news.xpath('./div/div/h3/a/text()').extract_first()
            article_url = news.xpath('./div/div/h3/a/@href').extract_first()

            title2 = news.xpath('./div/h3/a/text()').extract_first()
            article_url2 = news.xpath('./div/h3/a/@href').extract_first()

            title = title if title is not None else title2
            article_url = article_url if article_url is not None else article_url2

            article = {
                'img_url': img_url,
                'title' : title,
                'article_url': article_url
            }
            print(article)
        pass

    def close(spider, reason):
        spider.bro.close()