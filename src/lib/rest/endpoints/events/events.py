from flask import request
from flask_restx import Resource

from src.lib.db.db_utils import connect_to_db


class Events(Resource):
    def get(self, id=None):
        result = []
        conn = connect_to_db()
        cursor = conn.cursor()
        cmd = 'SELECT * FROM events WHERE id=%s' % id if id else 'SELECT * FROM events'
        cursor.execute(cmd)
        conn.commit()
        data = cursor.fetchall()
        if data is not None:
            for row in data:
                (id, name, description, image, links, event_type) = row
                result.append({
                    'id': id,
                    'name': name,
                    'description': description,
                    'image': bytes(image).decode('latin-1'),
                    'links': links,
                    'event_type': event_type
                })

        cursor.close()
        conn.close()
        return result

    def post(self):
        data = request.form
        name = data.get('name')
        description = data.get('description')
        image_file = request.files['image']
        binary_data = image_file.read()
        links = data.get('links')
        event_type = data.get('event_type')

        conn = connect_to_db()
        cursor = conn.cursor()
        cmd = "INSERT INTO events(name, description, image, links, event_type) VALUES " \
              "(%s, %s, %s, %s, %s)"
        cursor.execute(cmd, (name, description, binary_data, links, event_type))
        conn.commit()

        cursor.close()
        conn.close()

        return 'success'

    def put(self):
        return 'update'

    def delete(self):
        return 'delete'