import json
import logging

from flask import request
from flask_restx import Resource

from src.lib.db.db_utils import connect_to_db


class Authenticate(Resource):
    def get(self, email=None):
        resp = {}
        result = []
        error = None
        status_code = 200
        filters = {}

        if email:
            filters['email'] = email

        try:
            db = connect_to_db()
            data = db.get_entry('website_admin', filters)

            if data:
                for row in data:
                    (id, name, email, date_created) = row
                    result.append({
                        'id': id,
                        'name': name,
                        'email': email,
                        'date_created': date_created.strftime('%Y-%m-%d %H:%M:%S'),
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

        resp = 'success'
        status_code = 200
        try:
            db = connect_to_db()
            db.add_entry(
                'website_admin',
                ['name', 'email'],
                name, email
            )
        except Exception as e:
            resp = f'Something went wrong. Details: {e}'
            status_code = 500
            logging.error(resp)

        return resp, status_code

    def put(self, id):
        filters = {}
        filters['id'] = id
        data = request.form
        name = data.get('name')
        email = data.get('email')

        new_entry = {
            "name": name,
            "email": email
        }

        resp = 'success'
        status_code = 200
        try:
            db = connect_to_db()
            db.update_entry('website_admin', new_entry, filters)
        except Exception as e:
            resp = f'Something went wrong. Details: {e}'
            status_code = 500
            logging.error(resp)

        return resp, status_code

    def delete(self, id):
        filters={}
        filters['id'] = id

        resp = 'success'
        status_code = 200
        try:
            db = connect_to_db()
            db.delete_entry('website_admin', filters)
        except Exception as e:
            resp = f'Something went wrong. Details: {e}'
            status_code = 500
            logging.error(resp)

        return resp, status_code
