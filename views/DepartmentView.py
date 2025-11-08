

from flask import Flask
from flask import Blueprint
from controllers import department_controller


department_app= Blueprint("department_app",__name__)


#FUNCTIONALITY OF DEPARTMENT TABLE
@department_app.route("/adddepartment",methods = ['POST'])
def add_department():
   return department_controller.add_department()

@department_app.route("/getdepartment",methods = ['GET'])
def get_all_department():
   return department_controller.get_department()

@department_app.route("/getdepartment/<int:dept_id>",methods = ['GET'])
def get_department(dept_id):
   return department_controller.get_department_by_id(dept_id)

@department_app.route("/updatedepartment/<int:dept_id>",methods = ['PUT'])
def update_department(dept_id):
   return department_controller.update_dept_by_id(dept_id)

@department_app.route("/deletedepartment/<int:dept_id>",methods = ['DELETE'])
def delete_department(dept_id):
   return department_controller.delete_dept_by_id(dept_id)



if __name__ == '__main__':  
   department_app.run(debug=True)
