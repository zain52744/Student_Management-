from flask import request,jsonify
from models.teacher_model import TeacherModel

teacher_model = TeacherModel()

def add_teacher():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")

    teacher = teacher_model.add_teacher(name,email,phone)
    return jsonify(teacher)

def get_all_teachers():
    teachers = teacher_model.get_teacher()
    return jsonify(teachers)

def get_teach_by_id(teach_id):
    teacher = teacher_model.get_teacher_by_id(teach_id)
    if teacher:
        return jsonify(teacher)
    else:
        return("No record found")
    
def update_teach_by_id(teach_id):
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")

    teacher = teacher_model.update_teacher_by_id(teach_id,name,email,phone)
    if teacher:
        return jsonify(teacher)
    else:
        return("Record not found")
    
def delete_teach_by_id(teach_id):
    return teacher_model.delete_teacher_by_id(teach_id)