from flask import request
from flask_restx import Resource

from src.lib.db.db_utils import connect_to_db


class Careers(Resource):
    def get(self, id=None):
        result = []
        conn = connect_to_db()
        cursor = conn.cursor()
        cmd = 'SELECT * FROM careers WHERE id=%s' % id if id else 'SELECT * FROM careers'
        print(cmd)
        cursor.execute(cmd)
        conn.commit()
        data = cursor.fetchall()

        if data is not None:
            for row in data:
                (id, name, department, description, requirements, responsibilities, technologies, salary) = row
                result.append({
                    'id': id,
                    'name': name,
                    'department': department,
                    'description': description,
                    'requirements': requirements,
                    'responsibilities': responsibilities,
                    'technologies': technologies,
                    'salary': salary
                })

        cursor.close()
        conn.close()
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

        conn = connect_to_db()
        cursor = conn.cursor()
        cmd = "INSERT INTO careers(name, department, description, requirements, responsibilities, technologies, salary) VALUES (%s, %s, %s, " \
              "%s, %s, %s, %s)"
        cursor.execute(cmd, (name, department, description, requirements, responsibilities, technologies, salary,))
        conn.commit()

        cursor.close()
        conn.close()

        return 'success'

    def put(self):
        return 'update'

    def delete(self):
        return 'delete'