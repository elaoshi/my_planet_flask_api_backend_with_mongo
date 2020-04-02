

import pymongo 
import os


USERNAME = os.getenv('MONGODB_USERNAME', 'root')
PASSWORD = os.getenv('MONGODB_PASSWORD', 'example')
HOST = os.getenv('MONGO_HOST', 'mongo')
PORT = os.getenv('MONGO_PORT', 27017)

mng_client = pymongo.MongoClient(HOST,
        int(PORT),
        username=USERNAME,
        password=PASSWORD,
        maxPoolSize=200,
        waitQueueTimeoutMS=300
        )


mng_db = mng_client['demo'] # Replace mongo db name