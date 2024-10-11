# 3. Поэкспериментируйте с различными методами запросов.

from pymongo import MongoClient

filename = "log.txt"

with open(filename, "w", encoding='utf-8') as logname:
    client = MongoClient('mongodb://localhost:27017')
    db = client["library"]
    books = db.books
    duplicates = db.duplicates

    dbooks = duplicates.find({})
    for book in dbooks:
        print(book, file=logname)

    # фильтрация документов по критериям
    query = {"title": "The Star-Touched Queen"}
    docs = books.find(query)
    for doc in docs:
        print(f"Задвоение книг: {doc}", file=logname)

    print('\nКатегории книг', file=logname)
    # Выбрать категории
    categories = books.distinct("category")
    for i, category in enumerate(categories):
        print(f"{i}. {category}", file=logname)

    # Использование проекции
    print('\nКниги из категории Poetry', file=logname)
    query = {"category": "Poetry"}
    projection = {"title": 1, "price": 1, "_id": 0}
    proj_docs = books.find(query, projection)
    print("\n")
    for doc in proj_docs:
        print(doc, file=logname)

    print(file=logname)
    # Использование оператора $lt и $gte
    for price in range(0, 100, 10):
        query = {"$and": [{"price": {"$gt": price}}, {"price": {"$lt": price + 10}}]}
        print(f"Количество книг с ценой от {price} до {price + 10}: {books.count_documents(query)}", file=logname)

    # Использование оператора $regex
    query = {"title": {"$regex": "rain", "$options": "i"}}
    print(f"\nКоличество книг, содержащих 'rain': {books.count_documents(query)}", file=logname)

    # Использование оператора $in
    query = {"category": {"$in": ["Philosophy", "Womens Fiction"]}}
    print(f"Количество книг в категориях Philosophy, Womens Fiction: {books.count_documents(query)}", file=logname)

    # Использование оператора $all
    query = {"category": {"$all": ["Books", "Womens Fiction"]}}
    print(f"Количество книг в категориях сразу и Books и Womens Fiction: {books.count_documents(query)}",file = logname)

    # Использование оператора $ne
    query = {"category": {"$ne": "Books"}}
    print(f"Количество книг не в категории Books: {books.count_documents(query)}", file=logname)
