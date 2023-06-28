from flask_restx import Resource

from src.lib.db.db_utils import connect_to_db


class Newsletters(Resource):
    def get(self):
        result = []
        conn = connect_to_db()
        cursor = conn.cursor()
        cmd = 'SELECT * FROM newsletters'
        cursor.execute(cmd)
        conn.commit()
        data = cursor.fetchall()
        for row in data:
            (id, email) = row
            result.append({
                'id': id,
                'email': email
            })

        cursor.close()
        conn.close()
        return result

    def post(self, email):
        conn = connect_to_db()
        cursor = conn.cursor()
        cmd = f"INSERT INTO newsletters(email) VALUES (%s)"
        cursor.execute(cmd, (email,))
        conn.commit()

        cursor.close()
        conn.close()

        return 'success'