from pymongo import MongoClient
from ..config import Config

client = MongoClient(Config.MONGO_URI)
db = client[Config.MONGO_DB_NAME]
collection = db[Config.MONGO_COLLECTION_NAME]

def log_download_entry(user_name, image_name, timestamp):
    download_log = {"user_name": user_name, "image_name": image_name, "timestamp": timestamp}
    try:
        collection.insert_one(download_log)
        return True, "Download logged successfully!"
    except Exception as e:
        return False, str(e)
