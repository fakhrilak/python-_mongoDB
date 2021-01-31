import pymongo

def main():
    mongo =  pymongo.MongoClient("mongodb://localhost:27017")
    mydb =  mongo['pydb']
    coll = mydb['mycoll']
    exaple_update_all(coll)
    exaple_update_one(coll)


def exaple_update_one(coll):
    print("\n\n///////EDIT ONE///////")
    for value in coll.find():
        print("BEFORE EDIT : ",value)

    before = {"_id":3,"value":400}
    edit = {'$set':{"_id":3,"value":10000}}

    try:
        edited = coll.update_one(before,edit)
        for value in coll.find():
            print("\n EDITED",value)
    except Exception as e:
        print(e)


def exaple_update_all(coll):
    print("\n\n/////////EDIT ALL BESIC FUNC////////")
    for value in coll.find():
        print("BEFORE EDIT : ",value)

    myquery = { "type": { "$regex": "^I" } }
    newvalues = { "$set": { "name": "SENSOR SUHU" } }
    try:
        x = coll.update_many(myquery, newvalues)
        for value in coll.find():
            print("\n EDITED ",value)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
