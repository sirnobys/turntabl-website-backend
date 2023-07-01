import logging

from flask import request
from flask_restx import Resource

from src.lib.db.db_utils import connect_to_db


class CareerApplicants(Resource):
    def get(self, id=None, career_id=None):
        resp = {}
        result = []
        error = None
        status_code = 200
        filters = {}

        if id:
            filters['id'] = id
        if career_id:
            filters['career_id'] = career_id

        try:
            db = connect_to_db()
            data = db.get_entry('career_applicants', filters)

            if data:
                for row in data:
                    (id, career_id, first_name, last_name, email, cv, date_created) = row
                    result.append({
                        'id': id,
                        'career_id': career_id,
                        'first_name': first_name,
                        'last_name': last_name,
                        'email': email,
                        'cv': bytes(cv).decode('latin-1'),
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
        career_id = data.get('career_id')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        image_file = request.files['cv']
        binary_data = image_file.read()

        resp = 'success'
        status_code = 200

        try:
            db = connect_to_db()
            db.add_entry(
                'career_applicants',
                ['career_id', 'first_name', 'last_name', 'email', 'cv'],
                career_id, first_name, last_name, email, binary_data
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