from flask_restx import Namespace

from src.lib.rest.endpoints.careers.careers import Careers

api = Namespace('careers', description='', path='/api/careers/')
api.add_resource(Careers, '/', methods=['GET', 'POST', 'PUT', 'DELETE'])