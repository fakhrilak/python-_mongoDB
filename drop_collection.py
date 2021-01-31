import pymongo

mongo = pymongo.MongoClient("mongodb://localhost:27017")
mydb = mongo["pydb"]
collection = mydb["mycoll"]


collection.drop()

print(mydb.collection_names())
