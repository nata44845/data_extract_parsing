# Задание 1
# Установите пакет PyMongo и импортируйте MongoClient и json.
# Установите Compass MongoDB
# Подключитесь к серверу MongoDB по адресу 'mongodb://localhost:27017/'.
# Создайте базу данных 'town_cary' и коллекцию 'crashes'.
# Выполните чтение файла JSON 'crash-data.json'.
# Напишите функцию chunk_data, которая принимает два аргумента: список данных и размер фрагмента.
# Функция должна разделить данные на более мелкие фрагменты указанного размера и вернуть генератор.
# Разделите данные JSON на фрагменты по 5000 записей в каждом.
# Переберите все фрагменты и вставьте каждый фрагмент в коллекцию MongoDB с помощью функции insert_many().
# Выведите финальное сообщение, указывающее на то, что данные были успешно вставлены.

import json
from pymongo import MongoClient

# client = MongoClient('mongodb://localhost:27017')
client = MongoClient(
    'mongodb+srv://natashakachusova:mTiF6xl5M6LNLKuD@cluster0.0ub3h.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client["town_cary"]
crashes = db.crashes

with open("crash-data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# db.crashes.drop()
# crashes.insert_many(data["features"])

# i = 0
# for feature in data["features"]:
#     _id = feature.get("properties").get("tamainid")
#     feature['_id'] = _id
#     crashes.insert_one(feature)
#     i += 1
#     if (i % 5000 == 0):
#         print(i)

i=0
for doc in crashes.find({"properties.lat": {"$gt": 35, "$lt": 36},
                         "properties.lon": {"$gt": -79, "$lt": -78}
                         }
                        ):
    print(doc)
    i += 1

print(i)
print(crashes.count_documents({}))