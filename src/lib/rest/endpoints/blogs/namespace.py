from flask_restx import Namespace

from src.lib.rest.endpoints.blogs.blogs import Blogs


api = Namespace('blogs', description='', path='/api/blogs')
api.add_resource(Blogs, '/', methods=['GET', 'POST', 'PUT', 'DELETE'])