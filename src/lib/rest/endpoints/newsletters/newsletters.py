import logging

from flask_restx import Resource

from src.lib.db.db_utils import connect_to_db


class Newsletters(Resource):
    def get(self):
        resp = {}
        result = []
        error = None
        status_code = 200

        try:
            db = connect_to_db()
            data = db.get_entry('newsletters')

            if data:
                for row in data:
                    (id, email, date_created) = row
                    result.append({
                        'id': id,
                        'email': email,
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

    def post(self, email):
        resp = 'success'
        status_code = 200

        try:
            db = connect_to_db()
            db.add_entry('newsletters', ['email'], email)
        except Exception as e:
            resp = f'Something went wrong. Details: {e}'
            status_code = 500
            logging.error(resp)

        return resp, status_code
