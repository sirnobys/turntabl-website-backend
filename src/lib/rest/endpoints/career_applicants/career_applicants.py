from flask import request
from flask_restx import Resource

from src.lib.db.db_utils import connect_to_db


class CareerApplicants(Resource):
    def get(self, id=None):
        result = []
        conn = connect_to_db()
        cursor = conn.cursor()
        cmd = 'SELECT * FROM career_applicants WHERE id=%s' % id if id else 'SELECT * FROM career_applicants'
        cursor.execute(cmd)
        conn.commit()
        data = cursor.fetchall()

        if data is not None:
            for row in data:
                (id, career_id, first_name, last_name, email, cv) = row
                result.append({
                    'id': id,
                    'career_id': career_id,
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'cv': bytes(cv).decode('latin-1'),
                })

        cursor.close()
        conn.close()
        return result

    def post(self):
        data = request.form
        career_id = data.get('career_id')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        image_file = request.files['cv']
        binary_data = image_file.read()

        conn = connect_to_db()
        cursor = conn.cursor()
        cmd = "INSERT INTO career_applicants(career_id, first_name, last_name, email, cv) VALUES (%s, %s, %s, " \
              "%s, %s)"
        cursor.execute(cmd, (career_id, first_name, last_name, email, binary_data,))
        conn.commit()

        cursor.close()
        conn.close()

        return 'success'

    def put(self):
        return 'update'

    def delete(self):
        return 'delete'