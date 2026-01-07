from flask import Flask
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

print("done")





if __name__ == '__main__':  
   app.run(debug=True)
