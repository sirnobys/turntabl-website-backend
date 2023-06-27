from flask import Flask
from flask_restx import Api

from endpoints.newsletters.namespace import api as newletters_api
from endpoints.blogs.namespace import api as blogs_api
from endpoints.careers.namespace import api as careers_api
from endpoints.events.namespace import api as events_api

app = Flask(__name__)
api = Api(app, version='1.0', title='Turntabl Website API',
        description='API to manage website content')

api.add_namespace(newletters_api)
api.add_namespace(blogs_api)
api.add_namespace(careers_api)
api.add_namespace(events_api)

if __name__ == '__main__':
    app.run(debug=True)