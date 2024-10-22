# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose, Compose

def process_name(value):
    value=value[0].strip()
    return value

class PhotoparserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field(input_processor=Compose(process_name),output_processor=TakeFirst())
    categories = scrapy.Field()
    image_urls = scrapy.Field()
