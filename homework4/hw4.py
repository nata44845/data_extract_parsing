import requests
from lxml import html
from pprint import pprint
from time import sleep
import csv

headers = {
    "User-Agent": 'YaBrowser/24.7.6.970'}

url = 'https://news.mail.ru'
news_themes = ['economics','politics','society','incident']
# news_themes = ['economics']

item_list = []

for theme in news_themes:
    response = requests.get(url + '/'+theme, headers = headers)
    tree = html.fromstring(response.text)

    items = tree.xpath("//div[contains(@class,'newsitem_height_fixed')]")
    for item in items:
        item_info = {}
        name = item.xpath(".//span[@class='newsitem__title-inner']/text()")[0]
        link = item.xpath(".//a[contains(@class,'link-holder')]/@href")[0]
        text = item.xpath(".//span[@class='newsitem__text']//text()")[0]
        text = str(text).replace('\xa0',' ')
        item_info['theme'] = theme
        item_info['name'] = name
        item_info['link'] = link
        item_info['text'] = text
        item_list.append(item_info)

    sleep(1)

pprint(item_list)

csv_headers = ['theme','name','link', 'text']
with open("news.csv", 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=csv_headers)
    writer.writeheader()
    writer.writerows(item_list)
