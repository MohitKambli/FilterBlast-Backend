#from pymongo import MongoClient
import datetime
from ..config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..models.logs import Logs

'''client = MongoClient(Config.MONGO_URI)
db = client[Config.MONGO_DB_NAME]
collection = db[Config.MONGO_COLLECTION_NAME]'''

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

def log_download_entry(user_name, image_name):
    #download_log = {"user_name": user_name, "image_name": image_name, "timestamp": datetime.datetime.now()}
    try:
        #collection.insert_one(download_log)
        log_entry = Logs(user_name=user_name, image_name=image_name, timestamp=datetime.datetime.now())
        session.add(log_entry)
        session.commit()
        return True, "Download logged successfully!"
    except Exception as e:
        return False, str(e)
