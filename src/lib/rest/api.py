from flask import Flask
from flask_restx import Api
from flask_cors import CORS

from src.lib.rest.endpoints.v1.newsletters.namespace import api as newletters_api
from src.lib.rest.endpoints.v1.blogs.namespace import api as blogs_api
from src.lib.rest.endpoints.v1.careers.namespace import api as careers_api
from src.lib.rest.endpoints.v1.career_applicants.namespace import api as career_applicants_api
from src.lib.rest.endpoints.v1.events.namespace import api as events_api
from src.lib.rest.endpoints.v1.contact.namespace import api as contact_api
from src.lib.rest.endpoints.v1.authenticate.namespace import api as authenticate_api

app = Flask(__name__)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "http://localhost:3000"}})
api = Api(app, version='1.0', title='Turntabl Website API',
        description='API to manage website content')

api.add_namespace(newletters_api)
api.add_namespace(blogs_api)
api.add_namespace(careers_api)
api.add_namespace(career_applicants_api)
api.add_namespace(events_api)
api.add_namespace(contact_api)
api.add_namespace(authenticate_api)

if __name__ == '__main__':
    app.run(debug=True)