import pymongo
from pymongo import MongoClient
DATABASE_USER = "root"
DATABASE_PASSWORD= "root_password"
client= MongoClient(f"mongodb+srv://{DATABASE_USER}:{DATABASE_PASSWORD}@cluster0.4etijnx.mongodb.net/?retryWrites=true&w=majority")

database = client.test_db
collection = database.test_table

post = {
    "_id" : 2,
    "first_name" : "Varun",
    "last_name" : "Bainsla",
    "email" : "nbainsla21@gmial.com",
    "password" : "Varun@123"
}

data = collection.find()
for i in data:
    print(i)
    print(type(i))
