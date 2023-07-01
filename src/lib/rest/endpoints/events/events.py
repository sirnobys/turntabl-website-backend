from flask import request
from flask_restx import Resource

from src.lib.db.db_utils import connect_to_db


class Events(Resource):
    def get(self, id=None):
        result = []
        filters = {}
        db = connect_to_db()
        if id:
            filters['id'] = id
        data = db.get_entry('events', filters)

        if data is not None:
            for row in data:
                (id, name, description, image, links, status, date_created) = row
                result.append({
                    'id': id,
                    'name': name,
                    'description': description,
                    'image': bytes(image).decode('latin-1'),
                    'links': links,
                    'status': status,
                    'date_created': date_created.strftime('%Y-%m-%d %H:%M:%S')
                })

        return result

    def post(self):
        data = request.form
        name = data.get('name')
        description = data.get('description')
        image_file = request.files['image']
        binary_data = image_file.read()
        links = data.get('links')
        status = data.get('status')

        db = connect_to_db()
        result = db.add_entry(
            'events',
            ['name', 'description', 'image', 'links', 'status'],
            name, description, binary_data, links, status
        )

        return 'success' if result else 'failed'

    def put(self):
        return 'update'

    def delete(self):
        return 'delete'