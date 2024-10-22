# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import scrapy

class PhotoparserPipeline:

    def process_item(self, item, spider):
        with open('cats.csv', 'a', encoding='utf-8') as file:
            print(f"{item['name']}, {item['categories']},{item['image_urls']}", file=file)
        return item


class PhotoPipeline(ImagesPipeline):

    def get_media_requests(self, item, spider):
        print(item)
        if item['image_urls']:
            for img_url in item['image_urls']:
                try:
                    print(img_url)
                    yield scrapy.Request(img_url)
                except Exception as e:
                    print(e)
        return item

    def item_completed(self, results, item, info):
        if results:
            item['image_urls'] = [itm[1] for itm in results if itm[0]]
        return item
