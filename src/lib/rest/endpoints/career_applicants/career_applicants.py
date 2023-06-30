from flask import request
from flask_restx import Resource

from src.lib.db.db_utils import connect_to_db


class CareerApplicants(Resource):
    def get(self, id=None, career_id=None):
        result = []
        filters = {}

        if career_id:
            filters['career_id'] = career_id
        db = connect_to_db()
        data = db.get_entry('career_applicants', id, filters)

        if data is not None:
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

        return result

    def post(self):
        data = request.form
        career_id = data.get('career_id')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        image_file = request.files['cv']
        binary_data = image_file.read()

        db = connect_to_db()
        result = db.add_entry(
            'career_applicants',
            ['career_id', 'first_name', 'last_name', 'email', 'cv'],
            career_id, first_name, last_name, email, binary_data
        )

        return 'success' if result else 'failed'

    def put(self):
        return 'update'

    def delete(self):
        return 'delete'