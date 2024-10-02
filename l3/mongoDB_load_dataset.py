import gridfs
from pymongo import MongoClient
 
# client = MongoClient('mongodb://localhost:27017/')
client = MongoClient('mongodb+srv://natashakachusova:mTiF6xl5M6LNLKuD@cluster0.0ub3h.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
  
db = client["steam"]

collection = db["games"]

fs = gridfs.GridFS(db)
 
file_data =  open('steam_games.json', 'rb')
    
data = file_data.read()
fs.put(file_data, filename='steam_games.json')