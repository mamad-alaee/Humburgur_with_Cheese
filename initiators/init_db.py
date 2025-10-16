from mongoengine import connect
from initiators.init_env import load_db_env
db = None

async def connect_to_db():
    try:
        db_data = await load_db_env()
        global db
        db = connect(**db_data)
        print("Connected to database")
    except Exception as e:
        print(f"Error connecting to database: {e}")


async def close_db_connection():
    try:
        db.close()
        print("Database connection closed")
    except Exception as e:
        print(f"Error closing database connection: {e}")