from flask_restx import Namespace

from src.lib.rest.endpoints.v1.careers.careers import Careers

api = Namespace('careers', description='', path='/api/v1/careers')
api.add_resource(Careers, '/', methods=['GET', 'POST'])
api.add_resource(Careers, '/<id>', methods=['GET', 'PUT', 'DELETE'])