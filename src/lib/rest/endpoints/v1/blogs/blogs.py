import logging

from flask import request
from flask_restx import Resource

from src.lib.db.db_utils import connect_to_db


class Blogs(Resource):
    def get(self):
        resp = {}
        result = []
        error = None
        status_code = 200
        try:
            db = connect_to_db()
            data = db.get_entry('blogs')

            if data:
                for row in data:
                    (id, name, description, image, url, date_created) = row
                    result.append({
                        'id': id,
                        'name': name,
                        'description': description,
                        'image': bytes(image).decode('latin-1'),
                        'url': url,
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
        name = data.get('name')
        url = data.get('url')
        image_file = request.files['image']
        binary_data = image_file.read()
        description = data.get('description')

        resp = 'success'
        status_code = 200
        try:
            db = connect_to_db()
            db.add_entry(
                        'blogs',
                        ['name', 'description', 'image', 'url'],
                        name, url, binary_data, description
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