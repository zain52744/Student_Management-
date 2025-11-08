from db_helper import DBHelper

class StudentModel:
    def __init__(self):
        self.db = DBHelper()

    
    def add_student(self,name,email,phone,age,city):
        query = "INSERT INTO students (name,email,phone,age,city) VALUES (%s,%s,%s,%s,%s)"
        self.db.cursor.execute(query,(name,email,phone,age,city,))
        self.db.conn.commit()
        return("Student added successfully")
    
    def get_all_students(self):
        query = "SELECT * FROM students"
        self.db.cursor.execute(query,)
        return self.db.cursor.fetchall()

    def get_student_by_id(self, stu_id,):
        query = "SELECT * FROM students WHERE stu_id = %s"
        self.db.cursor.execute(query,(stu_id,))
        return self.db.cursor.fetchone()
    
    def update_student_by_id(self, stu_id,name,email,phone,age,city):
        query = "SELECT * FROM students WHERE stu_id = %s"
        self.db.cursor.execute(query,(stu_id,))
        student = self.db.cursor.fetchone()

        if student:
            update_query = """
                UPDATE students SET name=%s, email=%s, phone=%s, age=%s,city=%s
                WHERE stu_id=%s
"""
            self.db.cursor.execute(update_query,(name,email,phone,age,city,stu_id))
            self.db.conn.commit()
            return("Student updated successfully")
        else:
            return("Student not found")
        
    def delete_student_by_id(self, stu_id):
        query = "SELECT * FROM students WHERE stu_id = %s"
        self.db.cursor.execute(query,(stu_id,))
        student = self.db.cursor.fetchone()

        if student:
            delete_query = "DELETE FROM students WHERE stu_id = %s"
            self.db.cursor.execute(delete_query,(stu_id,))
            self.db.conn.commit()
            return("Student deleted successfully")
        else:
            return("Student not found")