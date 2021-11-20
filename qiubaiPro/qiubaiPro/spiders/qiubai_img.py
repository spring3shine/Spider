import scrapy
from qiubaiPro.items import QiubaiImgItem


class QiubaiImgSpider(scrapy.Spider):

    name = "qiubai_img"
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/imgrank/']

    def parse(self, response):
        articles = response.xpath("//*[@id=\"content\"]/div/div[2]/div")
        for article in articles:
            tag_id = article.xpath("./a[1]/@href").extract_first()
            content = article.xpath("./a[1]/div[1]/span").extract_first()
            img_src = article.xpath("./div[2]/a[1]/img[1]/@src").extract_first()

            item = QiubaiImgItem()
            item["tag_id"] = tag_id
            item["article_content"] = content
            item["img_src"] = img_src
            print(item)
            yield item

        pass
