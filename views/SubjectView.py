from flask import Blueprint
from controllers import subject_controller

subject_app = Blueprint("subject_app", __name__)


@subject_app.route("/addsubject",methods = ['POST'])
def add_subjects():
   return subject_controller.add_course()

@subject_app.route("/getsubjects",methods = ['GET'])
def get_all_subjects():
   return subject_controller.get_subjects()

@subject_app.route("/getsubject/<int:subj_id>",methods = ['GET'])
def get_subject_by_id(subj_id):
   return subject_controller.get_subj_by_id(subj_id)

@subject_app.route("/updatesubject/<int:subj_id>",methods = ['PUT'])
def update_subject_by_id(subj_id):
   return subject_controller.update_subj_by_id(subj_id)

@subject_app.route("/deletesubject/<int:subj_id>",methods = ['DELETE'])
def delete_subject_by_id(subj_id):
   return subject_controller.delete_subj_by_id(subj_id)