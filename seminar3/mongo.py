from pymongo import MongoClient

# client = MongoClient('mongodb://localhost:27017')
client = MongoClient(
    'mongodb+srv://natashakachusova:mTiF6xl5M6LNLKuD@cluster0.0ub3h.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client["users"]
persons = db.persons

doc = {
    "author": "Peter",
    

}