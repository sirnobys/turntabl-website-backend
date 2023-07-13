import logging

from flask import request
from flask_restx import Resource

from db.db_utils import connect_to_db


class Contact(Resource):
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
            data = db.get_entry('contact', filters)

            if data:
                for row in data:
                    (id, name, email, company, description, date_created) = row
                    result.append({
                        'id': id,
                        'name': name,
                        'email': email,
                        'company': company,
                        'description': description,
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
        email = data.get('email')
        company = data.get('company')
        description = data.get('description')

        resp = 'success'
        status_code = 200
        print(name)
        try:
            db = connect_to_db()
            db.add_entry(
                'contact',
                ['name', 'email', 'company', 'description'],
                name, email, company, description
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