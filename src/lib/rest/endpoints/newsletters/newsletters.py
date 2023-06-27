from flask_restx import Resource

class Newsletters(Resource):
    def get(self):
        return 'works'

    def post(self):
        return 'works as well'