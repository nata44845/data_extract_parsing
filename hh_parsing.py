# Выполнить скрейпинг данных в веб-сайта https://hh.ru/ и извлечь информацию о вакансиях
# по запросу вакансии по запросу Data Scientist, вакансию и зарплату, от, до, от и до, валюта
# Затем сохранить эту информацию в JSON-файле.
from time import sleep

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from pprint import pprint
import re

url = "https://hh.ru"


headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
params = {
    "search_field":"name",
    # "search_field": "company_name",
    # "search_field": "description",
    "text": "data scientist",
    "enable_snippets": "false",
    "L_save_area": "true",
    'page': 0
}

session = requests.session()
all_vacancies = []
response = session.get(url + "/search/vacancy", headers=headers, params=params)
soup = BeautifulSoup(response.text, "html.parser")
with open('hh1.html', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())

# vacancies1 = soup.find_all('div', {'data-qa': re.compile('vacancy-serp__vacancy')})
vacancies = soup.find_all('div', {'class': re.compile('vacancy-info--')})
print(len(vacancies))
# vacancy-serp__vacancy vacancy-serp__vacancy_standard_plus
# print(vacancies)
for item in vacancies:
    item_info = {}
    name_info = item.find('span', {'data-qa': 'serp-item__title-text'})
    item_info['name'] = name_info.getText()
    all_vacancies.append(item_info)

#         post_info['name'] = name_info.getText()
#         post_info['url'] = name_info.get('href')

# while True:
#     response = session.get(url + "/posts", headers=headers, params=params)
#     soup = BeautifulSoup(response.text, "html.parser")
#     posts = soup.find_all('div', {'class': 'post-item'})
#     if not posts:
#         break
#     for post in posts:
#         post_info = {}
#         name_info = post.find('a', {'class': 'post-item__title'})
#         post_info['name'] = name_info.getText()
#         post_info['url'] = name_info.get('href')
#
#         add_info = post.find('div', {'class': 'text-muted'}).findChildren('span')
#         post_info['views'] = int(add_info[0].getText())
#         post_info['comments'] = int(add_info[1].getText())
#         all_posts.append(post_info)
#     print(f"Обработана {params['page']} страница")
#     params['page'] += 1
pprint(all_vacancies)
pprint(len(all_vacancies))