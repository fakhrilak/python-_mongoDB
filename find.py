import pymongo

mongo = pymongo.MongoClient("mongodb://localhost:27017")
mydb = mongo['trypython']
print(mydb)
collection = mydb['pycollenctions']

x = collection.find_one()

print(x)
