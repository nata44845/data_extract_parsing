# 3. Сценарий Foursquare
# 4. Напишите сценарий на языке Python, который предложит пользователю ввести интересующую его категорию (например, кофейни, музеи, парки и т.д.).
# 5. Используйте API Foursquare для поиска заведений в указанной категории.
# 6. Получите название заведения, его адрес и рейтинг для каждого из них.
# 7. Скрипт должен вывести название и адрес и рейтинг каждого заведения в консоль.

import json
import requests

url = "https://api.foursquare.com/v3/places/search"

headers = {
    "Authorization": "fsq30crRa1ZQAJVqYBVlkdgrwI+D3NTu+kaZUfGlmBGnpIk=",
    "accept": "application/json"
}

city = input("Введите название города: ")
place = input("Введите категорию заведения (кофейни, музеи, парки и т.д): ")

params = {
    "near": city,
    "query": place,
    "fields": "name,location,rating"
}

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    print("Успешный запрос")
    data = json.loads(response.text)
    items = data["results"]
    for item in sorted(items, key = lambda item: item['name']):
        print(f"{item['name']}, адрес: {item['location'].get('formatted_address', 'не определен') \
        if item.get('location') else 'нет адреса'}, рейтинг {item.get('rating','не определен')}")
else:
    print("Запрос завершился ошибкой")
    print(response.status_code)