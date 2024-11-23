#from pymongo import MongoClient
import datetime
from ..config import Config
import psycopg2

'''client = MongoClient(Config.MONGO_URI)
db = client[Config.MONGO_DB_NAME]
collection = db[Config.MONGO_COLLECTION_NAME]'''

conn = psycopg2.connect(Config.SQLALCHEMY_DATABASE_URI)
cur = conn.cursor()

# Function to create the table if it does not exist
def create_logs_table():
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS logs (
        id SERIAL PRIMARY KEY,
        user_name VARCHAR(255) NOT NULL,
        image_name VARCHAR(255) NOT NULL,
        timestamp TIMESTAMP NOT NULL
    )
    '''
    cur.execute(create_table_query)
    conn.commit()  # Ensure the table creation query is executed

def log_download_entry(user_name, image_name):
    #download_log = {"user_name": user_name, "image_name": image_name, "timestamp": datetime.datetime.now()}
    try:
        #collection.insert_one(download_log)
        
        # Create the table if it doesn't exist
        create_logs_table()

        # Insert query with parameterized values
        cur.execute(
            '''
            INSERT INTO logs (user_name, image_name, timestamp)
            VALUES (%s, %s, %s)
            ''',
            (user_name, image_name, datetime.datetime.now())
        )
        # Commit the transaction
        conn.commit()
        return True, "Download logged successfully!"
    except Exception as e:
        return False, str(e)
