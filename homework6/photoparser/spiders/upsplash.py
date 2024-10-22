import scrapy
from scrapy.http import HtmlResponse
from ..items import PhotoparserItem
from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose

class UpsplashSpider(scrapy.Spider):
    name = "upsplash"
    allowed_domains = ["unsplash.com"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [f"https://unsplash.com/s/photos/{kwargs.get('query')}"]

    def parse(self, response):
        links = response.xpath("//a[@class='zNNw1']/@href").getall()
        for i, link in enumerate(links):
            links[i] = f"https://unsplash.com{link}"
        print(links)
        for link in links:
            yield response.follow(link, callback = self.parse_img)
        print()

    def parse_img(self, response: HtmlResponse):
        loader = ItemLoader(item=PhotoparserItem(), response=response)
        loader.default_input_processor = MapCompose(str.strip)

        name = response.xpath("//h1[@class='vev3s']/text()").get()
        loader.add_value('name', name)

        categories = response.xpath('//div[@class="zDHt2 N9mmz"]/a/text()').getall()
        loader.add_value('categories', categories)
        print()
        image_url = response.xpath("//div[@class='WxXog']/img/@src").get()
        loader.add_value('image_urls', image_url)


        yield loader.load_item()