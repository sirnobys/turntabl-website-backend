from flask_restx import Namespace

from endpoints.v1.blogs.blogs import Blogs


api = Namespace('blogs', description='', path='/api/v1/blogs')
api.add_resource(Blogs, '/', methods=['GET', 'POST', 'PUT', 'DELETE'])
api.add_resource(Blogs, '/<id>', methods=['GET', 'PUT', 'DELETE'])