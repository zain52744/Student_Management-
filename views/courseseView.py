
from flask import Flask
from controllers import student_controller
from controllers import department_controller
from controllers import course_controller
from controllers import teacher_controller
from controllers import subject_controller
from controllers import score_controller
from flask import Blueprint





course_app= Blueprint('course_app', __name__)



@course_app.route("/addcourse",methods = ['POST'])
def add_course():
   return course_controller.add_course()

@course_app.route("/getcourses",methods = ['GET'])
def get_courses():
   return course_controller.get_all_courses()

@course_app.route("/getcourse/<int:cour_id>",methods = ['GET'])
def get_course_by_id(cour_id):
   return course_controller.get_cour_by_id(cour_id)

@course_app.route("/updatecourse/<int:cour_id>",methods = ['PUT'])
def update_course(cour_id):
   return course_controller.update_course_by_id(cour_id)

@course_app.route("/deletecourse/<int:cour_id>",methods = ['DELETE'])
def delete_course(cour_id):
   return course_controller.delete_course_by_id(cour_id)

#FUNCTIONALITY OF TEACHER TABLE
@course_app.route("/addteacher",methods = ['POST'])
def add_teacher():
   return teacher_controller.add_teacher()

@course_app.route("/getteachers",methods = ['GET'])
def get_teachers():
   return teacher_controller.get_all_teachers()

@course_app.route("/getteacher/<int:teach_id>",methods = ['GET'])
def get_teacher(teach_id):
   return teacher_controller.get_teach_by_id(teach_id)

@course_app.route("/updateteacher/<int:teach_id>",methods= ['PUT'])
def update_teacher(teach_id):
   return teacher_controller.update_teach_by_id(teach_id)

@course_app.route("/deleteteacher/<int:teach_id>",methods = ['DELETE'])
def delete_teacher(teach_id):
   return teacher_controller.delete_teach_by_id(teach_id)

#FUNCTIONALITY OF SUBJECTS TABLE
@course_app.route("/addsubject",methods = ['POST'])
def add_subjects():
   return subject_controller.add_course()

@course_app.route("/getsubjects",methods = ['GET'])
def get_all_subjects():
   return subject_controller.get_subjects()

@course_app.route("/getsubject/<int:subj_id>",methods = ['GET'])
def get_subject_by_id(subj_id):
   return subject_controller.get_subj_by_id(subj_id)

@course_app.route("/updatesubject/<int:subj_id>",methods = ['PUT'])
def update_subject_by_id(subj_id):
   return subject_controller.update_subj_by_id(subj_id)

@course_app.route("/deletesubject/<int:subj_id>",methods = ['DELETE'])
def delete_subject_by_id(subj_id):
   return subject_controller.delete_subj_by_id(subj_id)

#FUNCTIONALITY OF SCORE TABLE
@course_app.route("/addscores", methods = ['POST'])
def add_scores():
   return score_controller.add_scores()

@course_app.route("/getscores",methods = ['GET'])
def get_all_scores():
   return score_controller.get_scores()

@course_app.route("/getscore/<int:sco_id>",methods = ['GET'])
def get_score_by_id(sco_id):
   return score_controller.get_sco_by_id(sco_id)

@course_app.route("/updatescore/<int:sco_id>",methods = ['PUT'])
def update_score_by_id(sco_id):
   return score_controller.update_sco_by_id(sco_id)

@course_app.route("/deletescore/<int:sco_id>",methods = ['DELETE'])
def delete_score_by_id(sco_id):
   return score_controller.delete_sco_by_id(sco_id)

if __name__ == '__main__':  
   course_app.run(debug=True)
