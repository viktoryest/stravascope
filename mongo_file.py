import pymongo
import os
from conf_var_func import config_vars

config_vars()

client = pymongo.MongoClient(
    os.environ.get('mongo_link')
)
db = client.stravascope
collection = db.settings
challenge_collections = db.challenges
if collection.estimated_document_count() == 0:
    collection.insert_one({
        "title": "last_challenge", "current_id": 2567
    })
