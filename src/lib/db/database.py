import psycopg2

class Database():
    def __init__(self, hostname, db_name, username, password, port):
        self.hostname = hostname
        self.db_name = db_name
        self.username = username
        self.password = password
        self.port = port
        self.conn = self.connect()

    def connect(self):
        return psycopg2.connect(
            host=self.hostname,
            dbname=self.db_name,
            user=self.username,
            password=self.password,
            port=self.port
        )