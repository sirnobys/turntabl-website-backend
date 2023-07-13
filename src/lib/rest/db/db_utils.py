import os
from dotenv import load_dotenv
from db.database import Database


def connect_to_db():
    load_dotenv()
    hostname = os.getenv('DB_HOSTNAME')
    db_name = os.getenv('DB_NAME')
    user_name = os.getenv('DB_USER_NAME')
    password = os.getenv('DB_PASSWORD')
    port = os.getenv('DB_PORT')

    return Database(hostname, db_name, user_name, password, port)