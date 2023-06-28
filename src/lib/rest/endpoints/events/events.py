from flask_restx import Resource

from src.lib.db.db_utils import connect_to_db


class Events(Resource):
    def get(self):
        result = []
        conn = connect_to_db()
        cursor = conn.cursor()
        cmd = 'SELECT * FROM events'
        cursor.execute(cmd)
        conn.commit()

        for row in cursor.fetchall():
            (id, title, url, image, description) = row
            result.append({
                'id': id,
                'title': title,
                'url': url,
                'image': image,
                'description': description
            })

        cursor.close()
        conn.close()
        return result

    def post(self, title, url, image, description):
        conn = connect_to_db()
        cursor = conn.cursor()
        cmd = f"INSERT INTO events(title, url, image, description) VALUES " \
              f"('{title}', '{url}', '{image}', '{description}')"
        cursor.execute(cmd)
        conn.commit()

        cursor.close()
        conn.close()

        return 'success'

    def put(self):
        return 'update'

    def delete(self):
        return 'delete'