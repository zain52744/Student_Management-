from flask import Blueprint
from controllers import teacher_controller

teacher_app = Blueprint("teacher_app", __name__)

@teacher_app.route("/addteacher",methods = ['POST'])
def add_teacher():
   return teacher_controller.add_teacher()

@teacher_app.route("/getteachers",methods = ['GET'])
def get_teachers():
   return teacher_controller.get_all_teachers()

@teacher_app.route("/getteacher/<int:teach_id>",methods = ['GET'])
def get_teacher(teach_id):
   return teacher_controller.get_teach_by_id(teach_id)

@teacher_app.route("/updateteacher/<int:teach_id>",methods= ['PUT'])
def update_teacher(teach_id):
   return teacher_controller.update_teach_by_id(teach_id)

@teacher_app.route("/deleteteacher/<int:teach_id>",methods = ['DELETE'])
def delete_teacher(teach_id):
   return teacher_controller.delete_teach_by_id(teach_id)