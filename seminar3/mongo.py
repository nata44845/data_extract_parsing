from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError, BulkWriteError

# client = MongoClient('mongodb://localhost:27017')
client = MongoClient(
    'mongodb+srv://natashakachusova:mTiF6xl5M6LNLKuD@cluster0.0ub3h.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client["users"]
persons = db.persons
duplicates = db.duplicates

doc = [{"_id": "1",
        "author": "John",
        "age": 29,
        "text": "is cool! Strawberry",
        "tags": ["ice"],
        "date": "04.08.1971"
        },
       {"_id": "2",
        "author": "Anna",
        "age": 30,
        "text": "is cool! Wildberry",
        "tags": ["cool", "hot", "ice"],
        "date": "26.01.1983"
        },
       {"_id": "123",
        "author": "Peter",
        "age": 30,
        "text": "is cool! Wildberry",
        "tags": ["cool", "hot", "ice"],
        "date": "14.06.1983"
        }
       ]

for item in doc:
    try:
        # persons.insert_one(doc)
        # persons.insert_many(doc)
        persons.insert_one(item)
    except DuplicateKeyError as e:
        try:
            duplicates.insert_one(item)
        except:
            print(f"{e}")
    except BulkWriteError as e:
        print(f"{e}")

print()

new_data = {
    "author": "Mikl",
    "text": "is cool! Raspberry"
}

# Обновить одного, меняет по тегам
persons.update_one({"author": "Petya"}, {"$set": new_data})

# Заменить одного, меняет целиком
persons.replace_one({"author": "Petya"}, {"author": "Andrey"})

persons.delete_one({"author": "Andrey"})

#for doc in persons.find({"$or":[{"author": "John"},{"age": {"$gt":29}}]}):
for doc in persons.find({"author": {"$regex": "A."}},{"_id": 0}).sort("_id"): #не выводить id
    print(doc)


