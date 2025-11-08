from flask import request,jsonify
from models.course_model import CourseModel

course_model = CourseModel()

def add_course():
    data = request.get_json()
    dept_id = data.get("dept_id")
    cour_name = data.get("cour_name")
    duration = data.get("duration")

    course = course_model.add_course(dept_id,cour_name,duration)
    return jsonify(course)

def get_all_courses():
    courses = course_model.get_courses()

    if courses:
        return jsonify(courses)
    else:
        return("No course found")
    
def get_cour_by_id(cour_id):
    course = course_model.get_course_by_id(cour_id)

    if course:
        return jsonify(course)
    else:
        return("Course not found")
    
def update_course_by_id(cour_id):
    data = request.get_json()
    dept_id = data.get("dept_id")
    cour_name = data.get("cour_name")
    duration = data.get("duration")

    course = course_model.update_course(cour_id,dept_id,cour_name,duration)

    if course:
        return jsonify(course)
    else:
        return("Course not found")
    
def delete_course_by_id(cour_id):
    return course_model.delete_course(cour_id)

