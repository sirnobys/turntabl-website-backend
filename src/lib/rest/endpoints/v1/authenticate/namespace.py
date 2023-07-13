from flask_restx import Namespace

from endpoints.v1.authenticate.authenticate import Authenticate

api = Namespace('authenticate', description='', path='/api/v1/authenticate')
api.add_resource(Authenticate, '/', methods=['GET', 'POST'])
api.add_resource(Authenticate, '/<email>', methods=['GET', 'PUT', 'DELETE'])
api.add_resource(Authenticate, '/<id>', methods=['DELETE'])