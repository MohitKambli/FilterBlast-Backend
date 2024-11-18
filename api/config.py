import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_URI = os.getenv("MONGO_URI")
    MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
    MONGO_COLLECTION_NAME = os.getenv("MONGO_COLLECTION_NAME")
    AWS_REGION = os.getenv("AWS_REGION")
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_S3_BUCKET_NAME = os.getenv("AWS_S3_BUCKET_NAME")
    REDIS_HOST = os.getenv("REDIS_HOST"),
    REDIS_PORT = os.getenv("REDIS_PORT"),
    REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
