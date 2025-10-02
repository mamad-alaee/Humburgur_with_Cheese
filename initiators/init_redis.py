from redis.asyncio import Redis

async def connect_redis():
    try:
        redis_client = Redis.from_url(
            "redis://localhost:6379",
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
