import os
from dotenv import load_dotenv



async def load_db_env():
    load_dotenv()
    db_data = {
        "db":os.getenv("DB"),
        "host":os.getenv("HOST"),
        "port":int(os.getenv("PORT")),
    }
    return db_data
    
    
    

async def load_jwt_key_env():
    load_dotenv()
    return os.getenv("JWT_KEY")

async def load_redis_env():
    load_dotenv()
    return os.getenv("REDIS_ADDRESS")