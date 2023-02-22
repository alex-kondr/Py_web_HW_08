import configparser
from pathlib import Path

from mongoengine import connect


path = Path(__file__).parent
# print(path)

config = configparser.ConfigParser()
config.read(path.joinpath("config.ini"))

mongo_user = config.get("DB", "user")
mongo_pass = config.get("DB", "pass")
db_name = config.get("DB", "db_name")
domain = config.get("DB", "domain")
# print(mongo_user)

connect(host=f"mongodb+srv://{mongo_user}:{mongo_pass}@{domain}/{db_name}", ssl=True)


# client = pymongo.MongoClient("mongodb+srv://alex_kondr:ZooaYEv5hW1wWDJR@cluster0.7yug6x4.mongodb.net/MyMongoDB_test?retryWrites=true&w=majority")
# db = client.test
# print(db)
