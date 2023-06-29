from flask import request
from flask_restx import Resource

from src.lib.db.db_utils import connect_to_db


class Blogs(Resource):
    def get(self):
        result = []
        conn = connect_to_db()
        cursor = conn.cursor()
        cmd = 'SELECT * FROM blogs'
        cursor.execute(cmd)
        conn.commit()
        data = cursor.fetchall()

        if data is not None:
            for row in data:
                (id, name, url, image, description) = row
                result.append({
                    'id': id,
                    'name': name,
                    'url': url,
                    'image': bytes(image).decode('latin-1'),
                    'description': description
                })

        cursor.close()
        conn.close()
        return result

    def post(self):
        data = request.form
        name = data.get('name')
        url = data.get('url')
        image_file = request.files['image']
        binary_data = image_file.read()
        description = data.get('description')

        conn = connect_to_db()
        cursor = conn.cursor()
        cmd = "INSERT INTO blogs(name, url, image, description) VALUES (%s, %s, %s, %s)"
        cursor.execute(cmd, (name, url, binary_data, description,))
        conn.commit()

        cursor.close()
        conn.close()

        return 'success'

    def put(self):
        return 'update'

    def delete(self):
        return 'delete'