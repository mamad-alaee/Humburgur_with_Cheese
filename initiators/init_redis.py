from redis.asyncio import Redis
from initiators.init_env import load_redis_env

async def connect_redis():
    redis_url = await load_redis_env()
    try:
        redis_client = Redis.from_url(
            redis_url,
            encoding="utf-8",
            decode_responses=True,
        )
        print("Redis connected successfully")
        return redis_client
    except Exception as e:
        print("Error connecting to Redis: ", e)
        return None



async def close_redis(redis_client):
    try:
        await redis_client.close()
        print("Redis connection closed successfully")
    except Exception as e:
        print("Error closing Redis connection: ", e)
