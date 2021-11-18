import scrapy
from scrapy.http import HtmlResponse

from qiubaiPro.items import QiubaiproItem


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    url_base = 'https://www.qiushibaike.com'
    url_page_temp = 'https://www.qiushibaike.com/text/page/{}'
    page_num = 1

    # def parse(self, response: HtmlResponse):
    #     """
    #         该方法用于测试：通过终端命令进行持久化,命令为scrapy crawl qiubai -o qiubai_dic.csv
    #     :param response:
    #     :return:
    #     """
    #     div_list = response.xpath("//*[@id=\"content\"]/div/div[2]/div")
    #     for div in div_list:
    #         # print(div)
    #         qiushi_tag_id = div.xpath("./@id")[0].extract() # 段子id
    #         author_img =  div.xpath("./div[1]/a[1]/img[1]/@src")[0].extract() # 作者图片链接
    #         author_name = div.xpath("./div[1]/a[1]/img[1]/@alt")[0].extract() # 作者名
    #         article = div.xpath("./a[1]/div[1]/span/text()").extract() # 文章内容
    #         article = ''.join(article)
    #         stats_vote = div.xpath("./div[2]/span[1]/i/text()")[0].extract() # 点赞数
    #         stats_comments = div.xpath("./div[2]/span[2]/a/i/text()")[0].extract() # 评论数
    #         dic = {
    #             "tag_id" : qiushi_tag_id,
    #             "author_name": author_name,
    #             "author_img": author_img,
    #             "article": article,
    #             "stats_vote": stats_vote,
    #             "stats_comments": stats_comments
    #         }
    #         print(dic)
    #         yield dic
    #     pass

    def parse(self, response: HtmlResponse):
        """
            该方法用于测试：通过管道进行持久化
        :param response:
        :return:
        """
        div_list = response.xpath("//*[@id=\"content\"]/div/div[2]/div")
        for div in div_list:
            # print(div)
            qiushi_tag_id = div.xpath("./@id").extract_first()  # 段子id
            author_img = div.xpath("./div[1]/a[1]/img[1]/@src").extract_first()  # 作者图片链接
            author_name = div.xpath("./div[1]/a[1]/img[1]/@alt").extract_first()  # 作者名

            article_href = div.xpath("./a[1]/@href").extract_first()  # 文章详情链接
            article_content = div.xpath("./a[1]/div[1]/span[1]/text()").extract()  # 文章内容
            article_detail = div.xpath("./a[1]/div[1]/span[2]/text()").extract_first()  # 文章内容
            article = ''.join(article_content)

            stats_vote = div.xpath("./div[2]/span[1]/i/text()").extract_first()  # 点赞数
            stats_comments = div.xpath("./div[2]/span[2]/a/i/text()").extract_first()  # 评论数

            item = QiubaiproItem()
            item['tag_id'] = qiushi_tag_id
            item['author_name'] = author_name
            item['author_img'] = author_img
            item['article'] = article
            item['stats_vote'] = stats_vote
            item['stats_comments'] = stats_comments
            print(item, '\n\n\n')

            if '查看全文' == article_detail:
                yield scrapy.Request(url=self.url_base + article_href, callback=self.parse_article_detail, meta={"item": item})
            else:
                yield item

        # 对前三页进行爬取
        if self.page_num < 3:
            self.page_num += 1
            new_url = self.url_page_temp.format(self.page_num)
            yield scrapy.Request(url=new_url, callback=self.parse)

        pass

    def parse_article_detail(self, response):
        item = response.meta['item']
        article_content = response.xpath("//*[@id=\"single-next-link\"]/div").extract()
        article_content = ''.join(article_content)
        item['article'] = article_content
        yield item
