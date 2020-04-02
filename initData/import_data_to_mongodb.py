from bson import BSON


import sys, os

import json

import pymongo 

USERNAME = os.getenv('MONGODB_USERNAME', 'root')
PASSWORD = os.getenv('MONGODB_PASSWORD', 'example')
HOST = os.getenv('MONGO_HOST', 'localhost')
PORT = os.getenv('MONGO_PORT', 27017)

mng_client = pymongo.MongoClient(HOST,
        int(PORT),
        username=USERNAME,
        password=PASSWORD)

print("===> mongodb info: ",HOST,PASSWORD,HOST,PORT)

currentDir = os.path.dirname(os.path.abspath(__file__))

mng_db = mng_client['demo'] # Replace mongo db name

collection_name = 'companies' # Replace mongo db collection name
db_cm = mng_db[collection_name]
 
print("start to import companies data")
with open(currentDir+"/companies.json", 'r', encoding='utf-8') as json_data:
     data_json = json.load(json_data)

db_cm.remove()
db_cm.insert_many(data_json)

print("done") 
#----
print("start to import people data...")
collection_name = 'people' # Replace mongo db collection name
db_people = mng_db[collection_name]
 
people_json = ""
with open(currentDir + '/people.json', 'r', encoding='utf-8') as f:
    people_json = json.load(f)

db_people.remove()
db_people.insert_many(people_json)
print("done") 
