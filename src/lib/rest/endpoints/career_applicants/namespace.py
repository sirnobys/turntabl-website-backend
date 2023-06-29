from flask_restx import Namespace

from src.lib.rest.endpoints.career_applicants.career_applicants import CareerApplicants

api = Namespace('career-applicants', description='', path='/api/career-applicants')
api.add_resource(CareerApplicants, '/', methods=['GET', 'POST'])
api.add_resource(CareerApplicants, '/<id>', methods=['GET', 'DELETE'])
api.add_resource(CareerApplicants, '/career/<career_id>', methods=['GET', 'DELETE'])