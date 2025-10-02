from mongoengine import connect

db = None

async def connect_to_db():
    try:
        global db
        db = connect(
            db='humburgur_with_cheese',
            host="localhost",
            port = 27017
            )
        print("Connected to database")
    except Exception as e:
        print(f"Error connecting to database: {e}")


async def close_db_connection():
    try:
        db.close()
        print("Database connection closed")
    except Exception as e:
        print(f"Error closing database connection: {e}")