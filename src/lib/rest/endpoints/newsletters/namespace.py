from flask_restx import Namespace

from src.lib.rest.endpoints.newsletters.newsletters import Newsletters


api = Namespace('newsletters', description='', path='/api/newsletters/')
api.add_resource(Newsletters, '/', methods=['GET', 'POST', 'DELETE'])
