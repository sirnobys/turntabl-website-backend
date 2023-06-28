from flask import request
from flask_restx import Resource, fields

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
        for row in data:
            (id, title, url, image, description) = row
            result.append({
                'id': id,
                'title': title,
                'url': url,
                'image': bytes(image).decode('latin-1'),
                'description': description
            })

        cursor.close()
        conn.close()
        return result

    def post(self):
        data = request.form
        title = data.get('title')
        url = data.get('url')
        image_file = request.files['image']
        binary_data = image_file.read()
        description = data.get('description')

        conn = connect_to_db()
        cursor = conn.cursor()
        cmd = "INSERT INTO blogs(title, url, image, description) VALUES (%s, %s, %s, %s)"
        cursor.execute(cmd, (title, url, binary_data, description,))
        conn.commit()

        cursor.close()
        conn.close()

        return 'success'

    def put(self):
        return 'update'

    def delete(self):
        return 'delete'