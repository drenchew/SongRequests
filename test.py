from pymongo import MongoClient

# Connect to MongoDB
uri = "mongodb+srv://dre:dren4@songrq.vl0qg.mongodb.net/?retryWrites=true&w=majority&appName=songRq"

client = MongoClient(uri)
db = client["songRq"]  # Replace with your actual database name

# List all collections
collections = db.list_collection_names()

print("Collections in the database:", collections)


# add item to collection
collection = db["sessions"]
collection.insert_one({"session_id": "1", "password": "12"})

# find item in collection
item = collection.find_one({"session_id": "1", "password": "12"})
print("Item found:", item)

#search by provided session_id
item = collection.find_one({"session_id": "1"})
print("Item found by session_id:", item)

