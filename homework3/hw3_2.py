# 1. Установите MongoDB на локальной машине, а также зарегистрируйтесь в онлайн-сервисе. https://www.mongodb.com/ https://www.mongodb.com/products/compass

# mongod --dbpath "C:\Nata\python\MongoDB\Server\8.0\data" --logpath "C:\Nata\python\MongoDB\Server\8.0\log\log.log"
# 2. Загрузите данные который вы получили на предыдущем уроке путем скрейпинга сайта с помощью Buautiful Soup в MongoDB и создайте базу данных и коллекции для их хранения.

import json
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError, BulkWriteError

client = MongoClient('mongodb://localhost:27017')
db = client["library"]
books = db.books
duplicates = db.duplicates

books.drop()
duplicates.drop()

with open("books_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

i = 1
for item in data:
    if i % 100 == 0:
        print(i)
    item['_id'] = hash(item['category'] + item['title'])
    try:
        books.insert_one(item)
    except DuplicateKeyError as e:
        try:
            duplicates.insert_one(item)
        except:
            print(f"{e}")
    except BulkWriteError as e:
        print(f"{e}")
    i += 1

print(f"Загружено {books.count_documents({})}")
