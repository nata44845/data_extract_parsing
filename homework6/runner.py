from scrapy.crawler import CrawlerProcess
from scrapy.utils.reactor import install_reactor
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from photoparser.spiders.upsplash import UpsplashSpider

if __name__ == '__main__':
    configure_logging()
    install_reactor("twisted.internet.asyncioreactor.AsyncioSelectorReactor")
    with open('cats.csv', 'w', encoding='utf-8') as file:
        print(f"name, categories, image_urls", file=file)
    process = CrawlerProcess(get_project_settings())
    process.crawl(UpsplashSpider, query = 'cats')
    process.start()

