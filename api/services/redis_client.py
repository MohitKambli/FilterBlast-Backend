# redis_client.py
import redis
from ..config import Config

# Initialize the Redis client with your configuration
redis_client = redis.Redis(
    host=Config.REDIS_HOST,
    port=int(Config.REDIS_PORT),
    password=Config.REDIS_PASSWORD
)
