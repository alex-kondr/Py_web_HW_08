import pymongo


client = pymongo.MongoClient("mongodb+srv://alex_kondr:ZooaYEv5hW1wWDJR@cluster0.7yug6x4.mongodb.net/MyMongoDB_test?retryWrites=true&w=majority")
db = client.test
print(db)
