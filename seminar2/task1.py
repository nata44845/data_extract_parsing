# Задание 1. Соединение
# - установите библиотеку Beautiful Soup.
# - создайте новый сценарий Python и импортируйте библиотеку Beautiful Soup.
# - напишите код для запроса веб-страницы
# https://www.boxofficemojo.com/intl/?ref_=bo_nb_hm_tab
# с помощью библиотеки requests.
# - выведите HTML-содержимое веб-страницы в консоль

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
test_link = soup.find('a', {'class': 'a-link-normal'})
print(test_link)
