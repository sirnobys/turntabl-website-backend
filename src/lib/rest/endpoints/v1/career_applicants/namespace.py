from flask_restx import Namespace

from endpoints.v1.career_applicants.career_applicants import CareerApplicants

api = Namespace('career-applicants', description='', path='/api/v1/career-applicants')
api.add_resource(CareerApplicants, '/', methods=['GET', 'POST'])
api.add_resource(CareerApplicants, '/<id>', methods=['GET', 'DELETE'])
api.add_resource(CareerApplicants, '/career/<career_id>', methods=['GET', 'DELETE'])