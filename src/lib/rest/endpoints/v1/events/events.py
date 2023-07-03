import json
import logging

from flask import request
from flask_restx import Resource

from src.lib.db.db_utils import connect_to_db


class Events(Resource):
    def get(self, id=None):
        resp = {}
        result = []
        error = None
        status_code = 200
        filters = {}

        if id:
            filters['id'] = id

        try:
            db = connect_to_db()
            data = db.get_entry('events', filters)

            if data:
                for row in data:
                    (id, name, description, image, link, status, date_created) = row
                    result.append({
                        'id': id,
                        'name': name,
                        'description': description,
                        'image': bytes(image).decode('latin-1'),
                        'link': json.loads(link),
                        'status': status,
                        'date_created': date_created.strftime('%Y-%m-%d %H:%M:%S')
                    })
        except Exception as e:
            error = f'Something went wrong. Details: {e}'
            logging.error(error)

        resp['result'] = result
        if error:
            resp['error'] = error
            status_code = 500
        return resp, status_code

    def post(self):
        data = request.form
        print(data)
        name = data.get('name')
        description = data.get('description')
        image_file = request.files['image']
        binary_data = image_file.read()
        link = json.dumps(data.get('link'))
        status = data.get('status')
        resp = 'success'
        status_code = 200

        try:
            db = connect_to_db()
            db.add_entry(
                'events',
                ['name', 'description', 'image', 'link', 'status'],
                name, description, binary_data, link, status
            )
        except Exception as e:
            resp = f'Something went wrong. Details: {e}'
            status_code = 500
            logging.error(resp)

        return resp, status_code

    def put(self):
        return 'update'

    def delete(self):
        return 'delete'