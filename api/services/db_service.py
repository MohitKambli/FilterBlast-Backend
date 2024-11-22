#from pymongo import MongoClient
import datetime
from ..config import Config
import psycopg2

'''client = MongoClient(Config.MONGO_URI)
db = client[Config.MONGO_DB_NAME]
collection = db[Config.MONGO_COLLECTION_NAME]'''

conn = psycopg2.connect(Config.SQLALCHEMY_DATABASE_URI)
cur = conn.cursor()

def log_download_entry(user_name, image_name):
    #download_log = {"user_name": user_name, "image_name": image_name, "timestamp": datetime.datetime.now()}
    try:
        #collection.insert_one(download_log)
        # Insert query with parameterized values
        print('Cursor: ', cur)
        cur.execute(
            '''
            INSERT INTO logs (user_name, image_name, timestamp)
            VALUES (%s, %s, %s)
            ''',
            (user_name, image_name, datetime.datetime.now())
        )
        print("Hello, I am here!")
        # Commit the transaction
        conn.commit()
        return True, "Download logged successfully!"
    except Exception as e:
        return False, str(e)
