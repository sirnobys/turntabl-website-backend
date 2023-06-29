from flask_restx import Namespace

from src.lib.rest.endpoints.events.events import Events

api = Namespace('events', description='', path='/api/events')
api.add_resource(Events, '/', methods=['GET', 'POST'])
api.add_resource(Events, '/<id>', methods=['GET', 'PUT', 'DELETE'])