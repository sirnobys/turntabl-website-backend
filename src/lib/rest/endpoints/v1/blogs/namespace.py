from flask_restx import Namespace

from src.lib.rest.endpoints.v1.blogs.blogs import Blogs


api = Namespace('blogs', description='', path='/api/v1/blogs')
api.add_resource(Blogs, '/', methods=['GET', 'POST', 'PUT', 'DELETE'])