import pymongo

mongo = pymongo.MongoClient("mongodb://localhost:27017") ##add .databases_names() to show all names

getdb = mongo["pydb"]
collection = getdb["mycoll"] ##add .collection_names() to show all collection

data = [
    {
        "_id" : 1,
        "name" : "Sensor Suhu",
        "type" : "Input",
        "value": 300
    },
    {
        "_id"   : 2,
        "name"  : "LCD",
        "type"  : "Output"
    },
    {
        "_id" : 3,
        "name": "Sensor Cahaya",
        "type": "Input",
        "value":400
    }
]

x = collection.insert_many(data) ##use insert_one({name:"hello","value":45})
print(x)
