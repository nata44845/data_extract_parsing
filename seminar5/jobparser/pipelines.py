# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from operator import indexOf

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError, BulkWriteError

class JobparserPipeline:
    def __init__(self):
    #     client = MongoClient("localhost", 27017)
        client = MongoClient('mongodb://localhost:27017')
        self.mongo_base = client["vacancies"]

    def process_item(self, item, spider):
        coll = self.mongo_base[spider.name]
        item['_id'] = str(item['url']).split('?',1)[0].rsplit('/', 1)[-1]
        print()
        try:
            coll.insert_one(item)
        except DuplicateKeyError as e:
                print(f"{e}")
        except BulkWriteError as e:
            print(f"{e}")

        return item
