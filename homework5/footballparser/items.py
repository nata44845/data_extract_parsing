# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FootballparserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    num = scrapy.Field()
    name = scrapy.Field()
    country = scrapy.Field()
    coach = scrapy.Field()
    count = scrapy.Field()
    url = scrapy.Field()

