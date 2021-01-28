from datetime import datetime

import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
print(client)

print(client.list_database_names())
DB_TUTORIAL = "db_tutorial"
db = client[DB_TUTORIAL]
collection = db['test-collection']

res = collection.insert_one({"foo": "bar"})
print(res.inserted_id)


def user_factory(username: str, age: int) -> dict:
    """
    :param username:
    :param age:
    :return:
    """
    return {
        "username": username,
        "age": age,
        "created_time": datetime.now()
    }


users_collection = db['users']

users = [user_factory("moderator", 25), user_factory("admin", 28)]
users_collection.insert_many(users)
user_admin = users_collection.find_one({"username": "admin"})
print(user_admin, user_admin["_id"], user_admin["username"])