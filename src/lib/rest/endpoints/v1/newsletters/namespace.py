from flask_restx import Namespace

from endpoints.v1.newsletters.newsletters import Newsletters


api = Namespace('newsletters', description='', path='/api/v1/newsletters')
api.add_resource(Newsletters, '/subscribers/', methods=['GET'])
api.add_resource(Newsletters, '/subscriber/<email>', methods=['POST', 'DELETE'])
