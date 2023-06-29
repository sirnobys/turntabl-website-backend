from src.lib.db.database import Database


def connect_to_db():
    return Database('localhost', 'postgres', 'postgres', '1234', 5432)