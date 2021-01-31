import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["trypython"]
mycol = mydb["pycollenctions"]

mydict = { "_id":12,"name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)
