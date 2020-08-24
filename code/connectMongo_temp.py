from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
from random import randint

def connect_mongo(database_name,collection_name):
    ## info
    db_name = 'article'
    mongoDbUser='xxx'
    mongoDbPwd='xxx'

    mongo_url = "mongodb+srv://{user_name}:{pwd}@{url}/{dbname}?retryWrites=true&w=majority".format(user_name=mongoDbUser,pwd=mongoDbPwd,dbname=db_name)

    client = MongoClient(mongo_url)
    db=getattr(client,database_name)
    mongo_collections = getattr(db,collection_name)
    
    return mongo_collections

