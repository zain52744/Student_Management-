from flask import request,jsonify
from models.department_model import DepartmentModel

department_model = DepartmentModel()

def add_department():
    data = request.get_json()
    dept_name = data.get("dept_name")

    result = department_model.add_department(dept_name)
    return jsonify(result)

def get_department():
    department = department_model.get_all_department()
    return jsonify(department)

def get_department_by_id(dept_id): 
    department = department_model.get_department_by_id(dept_id)

    if department:
        return jsonify(department)
    else:
        return("Department not found")
    
def update_dept_by_id(dept_id):
    data = request.get_json()
    dept_name = data.get("dept_name")

    department = department_model.update_department_by_id(dept_id,dept_name)

    if department:
        return jsonify(department)
    else:
        return("Department not found")

def delete_dept_by_id(dept_id):
    return department_model.delete_department_by_id(dept_id)
