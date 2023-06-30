from flask_restx import Resource

from src.lib.db.db_utils import connect_to_db


class Newsletters(Resource):
    def get(self):
        result = []
        db = connect_to_db()
        data = db.get_entry('newsletters')

        if data is not None:
            for row in data:
                (id, email, date_created) = row
                result.append({
                    'id': id,
                    'email': email,
                    'date_created': date_created.strftime('%Y-%m-%d %H:%M:%S')
                })

        return result

    def post(self, email):
        db = connect_to_db()
        result = db.add_entry('newsletters', ['email'], email)

        return 'success' if result else 'failed'
