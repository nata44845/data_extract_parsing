# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class FootballparserPipeline:

    def process_item(self, item, spider):
        with open('football.csv', 'a', encoding='utf-8') as file:
            print(f"{item['num']}, {item['name']}, {item['country']}, {item['coach']}, {item['count']}, {item['url']}", file=file)
        return item
