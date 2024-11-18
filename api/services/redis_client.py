# redis_client.py
import redis
from ..config import Config

# Initialize the Redis client with your configuration
redis_client = redis.Redis(
    host=str(Config.REDIS_HOST),
    port=str(Config.REDIS_PORT),
    password=str(Config.REDIS_PASSWORD)
)
