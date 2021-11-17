import scrapy
from scrapy.http import HtmlResponse

from qiubaiPro.items import QiubaiproItem


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/']

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
            qiushi_tag_id = div.xpath("./@id")[0].extract()  # 段子id
            author_img = div.xpath("./div[1]/a[1]/img[1]/@src")[0].extract()  # 作者图片链接
            author_name = div.xpath("./div[1]/a[1]/img[1]/@alt")[0].extract()  # 作者名
            article = div.xpath("./a[1]/div[1]/span/text()").extract()  # 文章内容
            article = ''.join(article)
            stats_vote = div.xpath("./div[2]/span[1]/i/text()")[0].extract()  # 点赞数
            stats_comments = div.xpath("./div[2]/span[2]/a/i/text()")[0].extract()  # 评论数

            item = QiubaiproItem()
            item['tag_id'] = qiushi_tag_id
            item['author_name'] = author_name
            item['author_img'] = author_img
            item['article'] = article
            item['stats_vote'] = stats_vote
            item['stats_comments'] = stats_comments
            print(item,'\n\n\n')
            yield item
        pass
