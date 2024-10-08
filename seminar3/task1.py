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


from pymongo import MongoClient



client = MongoClient \
    ('mongodb+srv://natashakachusova:mTiF6xl5M6LNLKuD@cluster0.0ub3h.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
