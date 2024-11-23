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
        
        # Execute a DO block for table creation and record insertion
        cur.execute(
            '''
            DO $$
            BEGIN
                -- Create the table if it doesn't exist
                IF NOT EXISTS (SELECT 1 FROM information_schema.tables 
                               WHERE table_name = 'logs') THEN
                    CREATE TABLE logs (
                        id SERIAL PRIMARY KEY,
                        user_name VARCHAR(255) NOT NULL,
                        image_name VARCHAR(255) NOT NULL,
                        timestamp TIMESTAMP NOT NULL
                    );
                END IF;
                
                -- Insert the log entry
                INSERT INTO logs (user_name, image_name, timestamp)
                VALUES (%s, %s, %s);
            END $$;
            ''',
            (user_name, image_name, datetime.datetime.now())
        )
        # Commit the transaction
        conn.commit()
        return True, "Download logged successfully!"
    except Exception as e:
        return False, str(e)
