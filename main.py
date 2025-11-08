from flask import Flask
# from controllers import student_controller
# from controllers import department_controller
# from controllers import course_controller
# from controllers import teacher_controller
# from controllers import subject_controller
# from controllers import score_controller

from views.courseseView import course_app
from views.StudentViews import student_app
from views.DepartmentView import department_app
from views.TeacherView import teacher_app
from views.SubjectView import subject_app
from views.ScoreView import score_app

app = Flask(__name__)
app.register_blueprint(course_app, url_prefix= "/course")

app.register_blueprint(student_app, url_prefix = "/student")

app.register_blueprint(department_app, url_prefix = "/department")

app.register_blueprint(teacher_app, url_prefix= "/teacher")

app.register_blueprint(subject_app, url_prefix= "/subject")

app.register_blueprint(score_app, url_prefix= "/score")




# print(StudentViews.add_student())


# #API'S FOR STUDENT TABLE
# @app.route("/addstudent",methods = ['POST'])
# def add_student():
#    return student_controller.add_student()

# @app.route("/getstudents",methods = ['GET'])
# def get_all_students():
#    return student_controller.get_students()

# @app.route("/getstudent/<int:stu_id>",methods = ['GET'])
# def get_student(stu_id):
#    return student_controller.get_student_by_id(stu_id)


# @app.route("/updatestudent/<int:stu_id>",methods = ['PUT'])
# def update_student(stu_id):
#    return student_controller.update_stu_by_id(stu_id)

# @app.route("/deletestudent/<int:stu_id>",methods = ['DELETE'])
# def delete_student(stu_id):
#    return student_controller.delete_student_by_id(stu_id)

# #FUNCTIONALITY OF DEPARTMENT TABLE
# @app.route("/adddepartment",methods = ['POST'])
# def add_department():
#    return department_controller.add_department()

# @app.route("/getdepartment",methods = ['GET'])
# def get_all_department():
#    return department_controller.get_department()

# @app.route("/getdepartment/<int:dept_id>",methods = ['GET'])
# def get_department(dept_id):
#    return department_controller.get_department_by_id(dept_id)

# @app.route("/updatedepartment/<int:dept_id>",methods = ['PUT'])
# def update_department(dept_id):
#    return department_controller.update_dept_by_id(dept_id)

# @app.route("/deletedepartment/<int:dept_id>",methods = ['DELETE'])
# def delete_department(dept_id):
#    return department_controller.delete_dept_by_id(dept_id)

# #FUNIONALITY OF COURSE TABLE
# @app.route("/addcourse",methods = ['POST'])
# def add_course():
#    return course_controller.add_course()

# @app.route("/getcourses",methods = ['GET'])
# def get_courses():
#    return course_controller.get_all_courses()

# @app.route("/getcourse/<int:cour_id>",methods = ['GET'])
# def get_course_by_id(cour_id):
#    return course_controller.get_cour_by_id(cour_id)

# @app.route("/updatecourse/<int:cour_id>",methods = ['PUT'])
# def update_course(cour_id):
#    return course_controller.update_course_by_id(cour_id)

# @app.route("/deletecourse/<int:cour_id>",methods = ['DELETE'])
# def delete_course(cour_id):
#    return course_controller.delete_course_by_id(cour_id)

# #FUNCTIONALITY OF TEACHER TABLE
# @app.route("/addteacher",methods = ['POST'])
# def add_teacher():
#    return teacher_controller.add_teacher()

# @app.route("/getteachers",methods = ['GET'])
# def get_teachers():
#    return teacher_controller.get_all_teachers()

# @app.route("/getteacher/<int:teach_id>",methods = ['GET'])
# def get_teacher(teach_id):
#    return teacher_controller.get_teach_by_id(teach_id)

# @app.route("/updateteacher/<int:teach_id>",methods= ['PUT'])
# def update_teacher(teach_id):
#    return teacher_controller.update_teach_by_id(teach_id)

# @app.route("/deleteteacher/<int:teach_id>",methods = ['DELETE'])
# def delete_teacher(teach_id):
#    return teacher_controller.delete_teach_by_id(teach_id)

# #FUNCTIONALITY OF SUBJECTS TABLE
# @app.route("/addsubject",methods = ['POST'])
# def add_subjects():
#    return subject_controller.add_course()

# @app.route("/getsubjects",methods = ['GET'])
# def get_all_subjects():
#    return subject_controller.get_subjects()

# @app.route("/getsubject/<int:subj_id>",methods = ['GET'])
# def get_subject_by_id(subj_id):
#    return subject_controller.get_subj_by_id(subj_id)

# @app.route("/updatesubject/<int:subj_id>",methods = ['PUT'])
# def update_subject_by_id(subj_id):
#    return subject_controller.update_subj_by_id(subj_id)

# @app.route("/deletesubject/<int:subj_id>",methods = ['DELETE'])
# def delete_subject_by_id(subj_id):
#    return subject_controller.delete_subj_by_id(subj_id)

# #FUNCTIONALITY OF SCORE TABLE
# @app.route("/addscores", methods = ['POST'])
# def add_scores():
#    return score_controller.add_scores()

# @app.route("/getscores",methods = ['GET'])
# def get_all_scores():
#    return score_controller.get_scores()

# @app.route("/getscore/<int:sco_id>",methods = ['GET'])
# def get_score_by_id(sco_id):
#    return score_controller.get_sco_by_id(sco_id)

# @app.route("/updatescore/<int:sco_id>",methods = ['PUT'])
# def update_score_by_id(sco_id):
#    return score_controller.update_sco_by_id(sco_id)

# @app.route("/deletescore/<int:sco_id>",methods = ['DELETE'])
# def delete_score_by_id(sco_id):
#    return score_controller.delete_sco_by_id(sco_id)

if __name__ == '__main__':  
   app.run(debug=True)
