# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class MongodbPipeline(object):
    collection_name="Movie Stars"

    def open_spider(self,spider):
        self.client = pymongo.MongoClient("mongodb+srv://hemanth:h5m1n666@web-scrapping-1m160.mongodb.net/test?retryWrites=true&w=majority")
        self.db = self.client["Celeb_List"]

    def close_spider(self,spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(item)
        return item
