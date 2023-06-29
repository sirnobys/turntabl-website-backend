from flask import request
from flask_restx import Resource

from src.lib.db.db_utils import connect_to_db


class Events(Resource):
    def get(self, id=None):
        result = []
        db = connect_to_db()
        data = db.get_entry('events', id)

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

        return result

    def post(self):
        data = request.form
        name = data.get('name')
        description = data.get('description')
        image_file = request.files['image']
        binary_data = image_file.read()
        links = data.get('links')
        event_type = data.get('event_type')

        db = connect_to_db()
        result = db.add_entry(
            'events',
            ['name', 'description', 'image', 'links', 'event_type'],
            name, description, binary_data, links, event_type
        )

        status = 'failed'
        if result:
            status = 'success'
        return status

    def put(self):
        return 'update'

    def delete(self):
        return 'delete'