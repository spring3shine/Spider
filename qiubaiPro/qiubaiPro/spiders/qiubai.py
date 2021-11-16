import scrapy
from scrapy.http import HtmlResponse


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response: HtmlResponse):
        div_list = response.xpath("//*[@id=\"content\"]/div/div[2]/div")
        for div in div_list:
            # print(div)
            author_img =  div.xpath("./div[1]/a[1]/img[1]/@src")[0].extract() # 作者图片链接
            author_name = div.xpath("./div[1]/a[1]/img[1]/@alt")[0].extract() # 作者名
            article = div.xpath("./a[1]/div[1]/span/text()").extract() # 文章内容
            article = ''.join(article)
            stats_vote = div.xpath("./div[2]/span[1]/i/text()")[0].extract() # 点赞数
            stats_comments = div.xpath("./div[2]/span[2]/a/i/text()")[0].extract() # 评论数
            print(author_name)
            print(author_img)
            print(article)
            print(stats_vote,stats_comments)
            break
        pass

# //*[@id="content"]/div/div[2]/div[1]/div[1]/a[2]/h2