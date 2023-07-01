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

    def get_entry(self, table_name, filters={}):
        filter_items = [f'{k}={v}' for k, v in filters.items()]
        cmd = 'SELECT * FROM %s' % table_name
        if len(filter_items) != 0:
            cmd = cmd + ' WHERE ' + 'AND '.join(filter_items)
        cursor = self.conn.cursor()
        cursor.execute(cmd)
        self.conn.commit()
        result = cursor.fetchall()

        cursor.close()
        self.conn.close()

        return result

    def add_entry(self, table_name, columns, *args):
        values = ['%s'] * len(columns)
        cmd = f"INSERT INTO {table_name}({','.join(columns)}) VALUES ({','.join(values)})"
        cursor = self.conn.cursor()
        cursor.execute(cmd, (*args,))
        self.conn.commit()

        cursor.close()
        self.conn.close()
        return True
