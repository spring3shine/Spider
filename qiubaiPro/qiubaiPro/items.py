# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QiubaiproItem(scrapy.Item):
    # define the fields for your item here like:
    tag_id = scrapy.Field()
    author_name = scrapy.Field()
    author_img = scrapy.Field()
    article = scrapy.Field()
    stats_vote = scrapy.Field()
    stats_comments = scrapy.Field()
    pass
