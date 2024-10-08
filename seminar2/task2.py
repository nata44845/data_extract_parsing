# Задание 2. Список ссылок
# Напишите сценарий на языке Python, чтобы получить ссылки на релизы фильмов со страницы "International Box
# Office" на сайте Box Office Mojo.
# Сохраните ссылки в списке и выведите список на консоль.
# Требования:
# - Используйте библиотеку requests для запроса вебстраницы.
# - Используйте Beautiful Soup для парсинга HTMLсодержимого веб-страницы.
# - Найдите все ссылки в колонке #1 Release веб-страницы.
# - Используйте библиотеку urllib.parse для объединения ссылок с базовым URL.
# - Сохраните ссылки в списке и выведите список на консоль.
from pprint import pprint

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

url = "https://www.boxofficemojo.com"
ua = UserAgent()

headers = {"User-Agent": ua.random}
params = {"ref_": "bo_nb_hm_tab"}

session = requests.session()

response = session.get(url + '/intl', params=params, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
rows = soup.find_all('tr')

films = []
for row in rows[2:14]:
    film = {}
    area_info = row.find('td', {'class': 'mojo-field-type-area_id'}).findChildren()[0]
    # area_info = row.find('td', {'class': 'mojo-field-type-area_id'}).find('a')
    film['area'] = [area_info.getText(),url+area_info.get('href')]

    weekend_info = row.find('td', {'class': 'mojo-field-type-date_interval'}).findChildren()[0]
    film['weekend'] = [weekend_info.getText(), url + weekend_info.get('href')]

    film['realeses'] = int(row.find('td', {'class': 'mojo-field-type-positive_integer'}).getText())

    frelease_info = row.find('td', {'class': 'mojo-field-type-release'}).findChildren()[0]
    film['frelease'] = [frelease_info.getText(), url + frelease_info.get('href')]

    try:
        distributor_info = row.find('td', {'class': 'mojo-field-type-studio'}).findChildren()[0]
        film['distributor'] = [distributor_info.getText(), url + distributor_info.get('href')]
    except:
        print('Exception with frelease, object = ', film['frelease'])
        film['distributor'] = None

    film['gross'] = int(row.find('td', {'class': 'mojo-field-type-positive_integer'}).getText())

    films.append(film)

pprint(films)
