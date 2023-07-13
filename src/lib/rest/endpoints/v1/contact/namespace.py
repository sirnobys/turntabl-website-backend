from flask_restx import Namespace

from endpoints.v1.contact.contact import Contact

api = Namespace('contact', description='', path='/api/v1/contact')
api.add_resource(Contact, '/', methods=['GET', 'POST'])
api.add_resource(Contact, '/<id>', methods=['GET', 'DELETE'])
