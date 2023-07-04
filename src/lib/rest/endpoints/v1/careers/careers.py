import json
import logging

from flask import request
from flask_restx import Resource

from src.lib.db.db_utils import connect_to_db


class Careers(Resource):
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
            data = db.get_entry('careers', filters)

            if data:
                for row in data:
                    (id, name, department, description, requirements, responsibilities, technologies, salary, date_created) = row
                    result.append({
                        'id': id,
                        'name': name,
                        'department': department,
                        'description': description,
                        'requirements': requirements,
                        'responsibilities': responsibilities,
                        'technologies': technologies,
                        'salary': salary,
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
        department = data.get('department')
        description = data.get('description')
        requirements = json.loads(data.get('requirements'))
        responsibilities = json.loads(data.get('responsibilities'))
        technologies = json.loads(data.get('technologies'))
        salary = data.get('salary')

        resp = 'success'
        status_code = 200
        try:
            db = connect_to_db()
            db.add_entry(
                'careers',
                ['name', 'department', 'description', 'requirements', 'responsibilities', 'technologies', 'salary'],
                name, department, description, requirements, responsibilities, technologies, salary
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