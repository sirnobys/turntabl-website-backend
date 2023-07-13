from flask_restx import Namespace

from endpoints.v1.events.events import Events

api = Namespace('events', description='', path='/api/v1/events')
api.add_resource(Events, '/', methods=['GET', 'POST'])
api.add_resource(Events, '/<id>', methods=['GET', 'PUT', 'DELETE'])