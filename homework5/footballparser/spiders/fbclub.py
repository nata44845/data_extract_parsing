import scrapy
from scrapy.http import HtmlResponse
from ..items import FootballparserItem
from pprint import pprint

class FbclubSpider(scrapy.Spider):
    name = "fbclub"
    allowed_domains = ["www.sports.ru"]
    start_urls = ["https://www.sports.ru/football/club/"]

    def parse(self, response):
        next_page = response.xpath("//div[@class='pager']/a[last()]/@href").get()
        print(self.start_urls[0]+next_page)
        print()

        if next_page:
            yield response.follow(self.start_urls[0]+next_page, callback=self.parse)

        clubs = response.xpath("//table[contains(@class,'ratings-table')]/tbody/tr")
        for club in clubs:
            num = club.xpath(".//td[@class='alLeft']/text()").get()
            count = club.xpath(".//span[@class='count']/text()").get()
            link = club.xpath(".//div[@class='overBox']/a/@href").get()
            print(num, count, link)
            if link:
                yield response.follow(link,
                                    callback=self.club_parce,
                                    cb_kwargs = {'num': num,
                                                 'count': count
                                                 }
                )

    def club_parce(self, response: HtmlResponse, num, count):
        name = response.xpath("//h1//text()").get().strip()
        country = response.xpath("//table[@class='profile-table']/tr[1]/td[1]/text()").get()
        coach = response.xpath("//table[@class='profile-table']/tr[2]/td[1]/a/text()").get()
        url = response.url
        yield FootballparserItem(num = num, name=name, country=country, coach = coach, count = count, url=url)