import pymongo
from pymongo import MongoClient


def add(database, object):
    try:
        client = MongoClient('localhost', 27017)
        smartown = client.SmartTown
        db = client[database]
        add = db.insert_one(object).inserted_id
        if add != None:
            return True
        else:
            return False
    except:
        return False
