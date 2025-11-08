from flask import Flask
from flask import Blueprint
from controllers import student_controller


student_app = Blueprint("student_app",__name__)

#API'S FOR STUDENT TABLE
@student_app.route("/addstudent",methods = ['POST'])
def add_student():
   return student_controller.add_student()

@student_app.route("/getstudents",methods = ['GET'])
def get_all_students():
   return student_controller.get_students()

@student_app.route("/getstudent/<int:stu_id>",methods = ['GET'])
def get_student(stu_id):
   return student_controller.get_student_by_id(stu_id)


@student_app.route("/updatestudent/<int:stu_id>",methods = ['PUT'])
def update_student(stu_id):
   return student_controller.update_stu_by_id(stu_id)

@student_app.route("/deletestudent/<int:stu_id>",methods = ['DELETE'])
def delete_student(stu_id):
   return student_controller.delete_student_by_id(stu_id)




