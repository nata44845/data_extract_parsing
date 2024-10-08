# Выполнить скрейпинг данных в веб-сайта http://books.toscrape.com/
# и извлечь информацию о всех книгах на сайте во всех категориях:
# название, цену, количество товара в наличии (In stock (19 available)) в формате integer, описание.
# Затем сохранить эту информацию в JSON-файле.

import requests
from bs4 import BeautifulSoup
import json


def get_books_data(category, url):
    page = 1
    url_short = url[:url.rfind('/') + 1]
    print(url)
    books = []
    while True:
        if page == 1:
            response = requests.get(url)
        else:
            print(f"{url_short}page-{page}.html")
            response = requests.get(f"{url_short}page-{page}.html")
        soup = BeautifulSoup(response.content, 'html.parser')
        book_elements = soup.find_all('article', class_='product_pod')
        for element in book_elements:
            title = element.h3.a['title']
            price = float(element.find('p', class_='price_color').text[1:].replace('£', ''))

            # Получить ссылку на страницу с описанием товара
            description_link = element.find('h3').a['href']
            description_url = url.replace('index.html', '') + description_link

            description_response = requests.get(description_url)
            description_soup = BeautifulSoup(description_response.content, 'html.parser')

            stock_text = description_soup.find('p', class_='instock availability').text.strip()
            in_stock = int(''.join(filter(str.isdigit, stock_text))) if any(
                char.isdigit() for char in stock_text) else 0

            description = description_soup.find('article', class_='product_page').find_all('p')[3].text

            book = {
                'category': category,
                'title': title,
                'price': price,
                'in_stock': in_stock,
                'description': description
            }
            books.append(book)
        if not soup.find("li", {"class": "next"}):
            break
        page += 1
    return books


url = 'http://books.toscrape.com/'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
categories = soup.find('ul', class_='nav').find_all('li')

all_books = []

for category in categories:
    category_name = category.a.getText().strip()
    print(f"Обработка категории {category_name}")
    category_link = category.a['href']
    category_url = url + category_link
    books_data = get_books_data(category_name, category_url)
    all_books.extend(books_data)


# Сохраняем информацию в JSON-файле
with open('books_data.json', 'w', encoding='utf-8') as file:
    json.dump(all_books, file, ensure_ascii=False, indent=4)
