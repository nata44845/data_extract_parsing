# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline


class BookparserPipeline:
    def process_item(self, item, spider):
        print(item)
        print()
        return item

class BookPhotosPipeline(ImagesPipeline):

    def get_media_requests(self, item, spider):
        print(item)
        if item['photos']:
            for img_url in item['photos']:
                try:
                    print(img_url)
                    yield scrapy.Request(img_url)
                except Exception as e:
                    print(e)
        return item

    def item_completed(self, results, item, info):
        if results:
            item['photos'] = [itm[1] for itm in results if itm[0]]
        print()
        return item
