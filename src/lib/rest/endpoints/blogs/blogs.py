from flask_restx import Resource

class Blogs(Resource):
    def get(self):
        return 'get'

    def post(self):
        return 'works as well'

    def put(self):
        return 'update'

    def delete(self):
        return 'delete'