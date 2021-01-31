import pymongo

mongo = pymongo.MongoClient("mongodb://localhost:27017")
mydb = mongo["trypython"]
collection = mydb["pycollenctions"]

query = {"_id":12}
cari = collection.find(query)

for i in cari:
    print(i)
