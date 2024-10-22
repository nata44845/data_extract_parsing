import scrapy


class UpsplashSpider(scrapy.Spider):
    name = "upsplash"
    allowed_domains = ["unsplash.com"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [f"https://unsplash.com/s/photos/{kwargs.get('query')}"]

    def parse(self, response):
        pass

    # def parse(self, response):
    #     with open('book24.html', 'w', encoding='utf-8') as file:
    #         file.write(response.text)

    #     links = response.xpath("//a[@class='product-card__name']")
    #     print(links)
    #     for link in links:
    #         yield response.follow(link, callback = self.parse_book)
    #     print()

    # def parse_book(self, response: HtmlResponse):
    #     # name = response.xpath("//h1/text()").get()
    #     # price = response.xpath("//span[@class='app-price product-sidebar-price__price']/text()").get()
    #     # url = response.url
    #     # photos = response.xpath("//picture[@class='product-poster__main-picture']/source[1]/@srcset \
    #     #                     |//picture[@class ='product-poster__main-picture']/source[1]/@data-srcset"
    #     #     ).getall()
    #     # print(photos)
    #     # yield BookparserItem(name=name, price = price, url = url, photos = photos)
    #     loader = ItemLoader(item=BookparserItem(), response = response)
    #     loader.add_xpath('name', "//h1/text()")
    #     loader.add_xpath('price', "//span[@class='app-price product-sidebar-price__price']/text()")
    #     loader.add_value('url', response.url)
    #     loader.add_xpath('photos', "//picture[@class='product-poster__main-picture']/source[1]/@srcset \
    #                          |//picture[@class ='product-poster__main-picture']/source[1]/@data-srcset")
    #     yield loader.load_item()