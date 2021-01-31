import pymongo

mongo = pymongo.MongoClient("mongodb://localhost:27017") ##.database_names()
mydb = mongo["pydb"]
collection = mydb["mycoll"]

data = collection.find()
for i in data:
    print(i)

delet = {'test':'test'}
collection.delete_one(delet)
data = collection.find()
for value in data:
    print("\n\n AFTER DELET",value)
