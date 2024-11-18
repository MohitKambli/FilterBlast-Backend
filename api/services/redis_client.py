# redis_client.py
import redis
from ..config import Config

# Initialize the Redis client with your configuration
redis_client = redis.Redis(
    host=str(Config.REDIS_HOST),
    port=12367,
    password=str(Config.REDIS_PASSWORD)
)
