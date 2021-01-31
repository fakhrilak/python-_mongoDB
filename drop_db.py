import pymongo

mongo = pymongo.MongoClient("mongodb://localhost:27017")
mongo.drop_database("trypython")
