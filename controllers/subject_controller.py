from flask import request,jsonify
from models.subject_model import SubjectModel

subject_model = SubjectModel()

def add_course():
    data = request.get_json()
    stu_id = data.get("stu_id")
    teach_id = data.get("teach_id")
    cour_id = data.get("cour_id")
    subj_name = data.get("subj_name")

    course = subject_model.add_subjects(stu_id,teach_id,cour_id,subj_name)
    return jsonify(course)

def get_subjects():
    subjects = subject_model.get_all_subjects()
    return jsonify(subjects)

def get_subj_by_id(subj_id):
    subject = subject_model.get_subject_by_id(subj_id)

    if subject:
        return jsonify(subject)
    else:
        return ("Subject not found")
    
def update_subj_by_id(subj_id):
    data = request.get_json()
    stu_id = data.get("stu_id")
    teach_id = data.get("teach_id")
    cour_id = data.get("cour_id")
    subj_name = data.get("subj_name")

    subject = subject_model.update_subject_by_id(subj_id,stu_id,teach_id,cour_id,subj_name)
    if subject:
        return jsonify(subject)
    else:
        return("Subject not found")
    
def delete_subj_by_id(subj_id):
    return subject_model.delete_subject_by_id(subj_id)