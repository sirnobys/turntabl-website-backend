from flask_restx import Resource

from src.lib.db.db_utils import connect_to_db


class Newsletters(Resource):
    def get(self):
        result = []
        db = connect_to_db()
        data = db.get_entry('newsletters')

        if data is not None:
            for row in data:
                (id, email) = row
                result.append({
                    'id': id,
                    'email': email
                })

        return result

    def post(self, email):
        db = connect_to_db()
        result = db.add_entry('newsletters', ['email'], email)

        status = 'failed'
        if result:
            status = 'success'
        return status
