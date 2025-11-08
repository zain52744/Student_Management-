from db_helper import DBHelper

class CourseModel:
    def __init__(self):
        self.db = DBHelper()
    
    def add_course(self, dept_id,cour_name,duration):
        query = "INSERT INTO courses (dept_id,cour_name,duration) VALUES (%s,%s,%s)"
        self.db.cursor.execute(query,(dept_id,cour_name,duration,))
        self.db.conn.commit()
        return("Courses added successfully")
    
    def get_courses(self):
        query = "SELECT * FROM courses"
        self.db.cursor.execute(query,)
        return self.db.cursor.fetchall()

    def get_course_by_id(self, cour_id):
        query = "SELECT * FROM courses WHERE cour_id = %s"
        self.db.cursor.execute(query,(cour_id,))
        return self.db.cursor.fetchone()
    
    def update_course(self, cour_id,dept_id,cour_name,duration):
        query = "SELECT * FROM courses WHERE cour_id = %s"
        self.db.cursor.execute(query,(cour_id,))
        course = self.db.cursor.fetchone()

        if course:
            update_query = "UPDATE courses SET dept_id=%s, cour_name=%s,duration=%s WHERE cour_id=%s"
            self.db.cursor.execute(update_query,(dept_id,cour_name,duration,cour_id,))
            self.db.conn.commit()
            return ("Couese updated successfully")
        else:
            return "Course not found"
        
    def delete_course(self, cour_id):
        query = "SELECT * FROM courses WHERE cour_id = %s"
        self.db.cursor.execute(query,(cour_id,))
        course = self.db.cursor.fetchone()

        if course:
            delete_query = "DELETE FROM courses WHERE cour_id=%s"
            self.db.cursor.execute(delete_query,(cour_id,))
            self.db.conn.commit()
            return ("Course deleted succesfully")
        else:
            return("Course not found")