import pymongo
import pprint
import json
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['SmarTown']


def add(database, object):
    try:
        table = db[database]
        add = table.insert_one(object).inserted_id
        if add != None:
            return True
        else:
            return False
    except:
        return


def getall(database):
    try:
        table = db[database]
        print(database)
        array =[]
        for items in table.find({}):
            array.append(items)
        print(items)
        print(type(items))
        return items
    except Exception :
        print(Exception)
