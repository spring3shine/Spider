# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter


class QiubaiproPipeline:
    """
        持久化到本地txt文件
    """
    fp = None

    def open_spider(self, spider):
        print("start spider crawl...")
        self.fp = open('./qiubai.txt', 'w', encoding='utf-8')

    def close_spider(self, spider):
        print("ending spider....")
        self.fp.close()

    def process_item(self, item, spider):
        tag_id = item['tag_id']
        author_name = item['author_name']
        author_img = item['author_img']
        article = item['article']
        stats_vote = item['stats_vote']
        stats_comments = item['stats_comments']
        self.fp.write(tag_id + " " + author_name + " " + author_img + "\n")
        self.fp.write(article)
        self.fp.write(stats_vote + " " + stats_comments)
        return item


class QiubaiproDBPipeline:
    """
        向本地数据库进行持久化
    """
    conn = None
    cursor = None

    def __update_db_tag_id(self, item):
        assert self.conn.open
        print("updating...")
        tag_id = item['tag_id']
        author_name = item['author_name']
        author_img = item['author_img']
        article = item['article']
        stats_vote = item['stats_vote']
        stats_comments = item['stats_comments']
        self.cursor.execute("update spider.qiubai set author_name='{}',author_img = '{}', article='{}', stats_vote={},stats_comments={} where tag_id = '{}'}"
                            .format(author_name,author_img,article,stats_vote,stats_comments,tag_id))

    def __insert_db(self, item):
        assert self.conn.open
        print("inserting...")
        tag_id = item['tag_id']
        author_name = item['author_name']
        author_img = item['author_img']
        article = item['article']
        stats_vote = item['stats_vote']
        stats_comments = item['stats_comments']
        self.cursor.execute("insert into spider.qiubai(author_name,author_img,article,stats_vote,stats_comments,tag_id) values ('{}','{}','{}',{},{},'{}')"
                            .format(author_name,author_img,article,stats_vote,stats_comments,tag_id))


    def open_spider(self, spider):
        """
            准备数据库链接
        :param spider:
        :return:
        """
        try:
            print("connecting DB.....")
            self.conn = pymysql.Connect(host="localhost", user="root", password="123456")
            self.cursor = self.conn.cursor()
            print("connect Success !")
        except:
            print("connect Fail !")

        if not self.cursor.execute("show databases like 'spider'"):
            self.cursor.execute("create database spider")
        self.cursor.execute("use spider")

        if not self.cursor.execute("show tables like 'qiubai'"):
            self.cursor.execute("create table qiubai("
                                "id int auto_increment,"
                                "tag_id nvarchar(40) comment '段子id',"
                                "author_name nvarchar(40) comment '作者名',"
                                "author_img nvarchar(200) comment '作者头像',"
                                "article text comment '段子内容',"
                                "stats_comments int comment '评论数',"
                                "stats_vote int comment '点赞数',"
                                "primary key(id))engine Innodb default charset utf8mb4")

    def close_spider(self, spider):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        print("close DB connection")

    def process_item(self, item, spider):
        tag_id = item['tag_id']
        if self.cursor.execute("select * from spider.qiubai where tag_id = '{}'".format(tag_id)):
            self.__update_db_tag_id(item)
        else:
            self.__insert_db(item)
        return item
