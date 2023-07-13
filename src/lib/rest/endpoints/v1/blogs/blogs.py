import logging

from flask import request
from flask_restx import Resource

from db.db_utils import connect_to_db


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
                    (id, name, description, image, link, date_created) = row
                    result.append({
                        'id': id,
                        'name': name,
                        'description': description,
                        'image': bytes(image).decode('latin-1'),
                        'link': link,
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
        link = data.get('link')
        image_file = request.files['image']
        binary_data = image_file.read()
        description = data.get('description')

        resp = 'success'
        status_code = 200
        try:
            db = connect_to_db()
            db.add_entry(
                        'blogs',
                        ['name', 'description', 'image', 'link'],
                        name, description, binary_data, link
                      )
        except Exception as e:
            resp = f'Something went wrong. Details: {e}'
            status_code = 500
            logging.error(resp)

        return resp, status_code

    def put(self):
        return 'update'

    def delete(self, id):
        filters = {}
        filters['id'] = id

        resp = 'success'
        status_code = 200
        try:
            db = connect_to_db()
            db.delete_entry('blogs', filters)
        except Exception as e:
            resp = f'Something went wrong. Details: {e}'
            status_code = 500
            logging.error(resp)

        return resp, status_code