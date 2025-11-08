from flask import request,jsonify
from models.student_model import StudentModel

student_model = StudentModel()

def add_student():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")
    age = data.get("age")
    city = data.get('city')

    result = student_model.add_student(name,email,phone,age,city)
    return jsonify(result)

def get_students():
    students = student_model.get_all_students()
    return jsonify(students)

def get_student_by_id(stu_id):
    student = student_model.get_student_by_id(stu_id)
    if student:
        return jsonify(student)
    else:
        return("Student not found")

def update_stu_by_id(stu_id):
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")
    age = data.get("age")
    city = data.get('city')
    student = student_model.update_student_by_id(stu_id,name,email,phone,age,city)
    if student:
        return jsonify(student)
    else:
        return("Student not found")
    
def delete_student_by_id(stu_id):
    student = student_model.delete_student_by_id(stu_id)
    if student:
        return("Student deleted successfully")
    else:
        return("Student not found")