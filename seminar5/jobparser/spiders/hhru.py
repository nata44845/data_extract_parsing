import scrapy
from scrapy.http import HtmlResponse
from pprint import pprint
from jobparser.items import JobparserItem

class HhruSpider(scrapy.Spider):
    name = "hhru"
    allowed_domains = ["hh.ru"]
    start_urls = ["https://hh.ru/search/vacancy?area=54&hhtmFromLabel=rec_vacancy_show_all&hhtmFrom=main"]

    def parse(self, response: HtmlResponse):

        # with open('hh'+str(i)+'.html', 'w', encoding='utf-8') as file:
        #     print(response.text, file=file)

        next_page = response.xpath("//a[@data-qa='pager-next']/@href").get()
        print(next_page)
        print()

        if next_page:
            yield response.follow(next_page, callback=self.parse)

        links = response.xpath("//a[@data-qa='serp-item__title']/@href").getall()
        pprint(links)
        for link in links:
            yield response.follow(link, callback = self.vacancy_parce)


    def vacancy_parce(self, response: HtmlResponse):
        name = response.xpath("//h1//text()").get()
        salary = response.xpath("//div[@data-qa='vacancy-salary']//text()").getall()
        url = response.url
        yield JobparserItem(name=name, salary=salary, url=url)






