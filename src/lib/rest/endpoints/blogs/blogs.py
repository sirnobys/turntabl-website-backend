from flask import request
from flask_restx import Resource

from src.lib.db.db_utils import connect_to_db


class Blogs(Resource):
    def get(self):
        result = []
        db = connect_to_db()
        data = db.get_entry('blogs')

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

        return result

    def post(self):
        data = request.form
        name = data.get('name')
        url = data.get('url')
        image_file = request.files['image']
        binary_data = image_file.read()
        description = data.get('description')

        db = connect_to_db()
        result = db.add_entry(
                                'blogs',
                                ['name', 'url', 'image', 'description'],
                                name, url, binary_data, description
                              )

        status = 'failed'
        if result:
            status = 'success'
        return status

    def put(self):
        return 'update'

    def delete(self):
        return 'delete'