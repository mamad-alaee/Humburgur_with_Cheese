from mongoengine import connect

db = None

def connect_to_db():
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