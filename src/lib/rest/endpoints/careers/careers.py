from flask import request
from flask_restx import Resource

from src.lib.db.db_utils import connect_to_db


class Careers(Resource):
    def get(self, id=None):
        result = []
        db = connect_to_db()
        data = db.get_entry('careers', id)

        if data is not None:
            for row in data:
                (id, name, department, description, requirements, responsibilities, technologies, salary, date_created) = row
                result.append({
                    'id': id,
                    'name': name,
                    'department': department,
                    'description': description,
                    'requirements': requirements,
                    'responsibilities': responsibilities,
                    'technologies': technologies,
                    'salary': salary,
                    'date_created': date_created.strftime('%Y-%m-%d %H:%M:%S')
                })
        return result

    def post(self):
        data = request.json
        name = data.get('name')
        department = data.get('department')
        description = data.get('description')
        requirements = data.get('requirements')
        responsibilities = data.get('responsibilities')
        technologies = data.get('technologies')
        salary = data.get('salary')

        db = connect_to_db()
        result = db.add_entry(
            'careers',
            ['name', 'department', 'description', 'requirements', 'responsibilities', 'technologies', 'salary'],
            name, department, description, requirements, responsibilities, technologies, salary
        )

        return 'success' if result else 'failed'

    def put(self):
        return 'update'

    def delete(self):
        return 'delete'