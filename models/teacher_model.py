from db_helper import DBHelper

class TeacherModel:
    def __init__(self):
        self.db = DBHelper()

    def add_teacher(self, name,emial,phone):
        query = "INSERT INTO teachers(name,email,phone) VALUES(%s,%s,%s)"
        self.db.cursor.execute(query,(name,emial,phone,))
        self.db.conn.commit()
        return("Teacher added successfully")
    
    def get_teacher(self):
        query = "SELECT * FROM teachers"
        self.db.cursor.execute(query,)
        return self.db.cursor.fetchall()
    
    def get_teacher_by_id(self, teach_id):
        query = "SELECT * FROM teachers WHERE teach_id = %s"
        self.db.cursor.execute(query,(teach_id,))
        return self.db.cursor.fetchone()

    def update_teacher_by_id(self,teach_id,name,email,phone):
        query = "SELECT * FROM teachers WHERE teach_id=%s"
        self.db.cursor.execute(query,(teach_id,))
        teacher = self.db.cursor.fetchone()
        if teacher:
            update_query = """
                UPDATE teachers SET name=%s, email=%s, phone=%s
                WHERE teach_id=%s
"""
            self.db.cursor.execute(update_query,(name,email,phone,teach_id,))
            self.db.conn.commit()
            return("Teacher updated succesfully")
        else:
            return("Record not found")
        
    def delete_teacher_by_id(self, teach_id):
        query = "SELECT * FROM teachers WHERE teach_id = %s"
        self.db.cursor.execute(query,(teach_id,))
        teacher = self.db.cursor.fetchone()

        if teacher:
            delete_query = "DELETE FROM teachers WHERE teach_id=%s"
            self.db.cursor.execute(delete_query,(teach_id,))
            self.db.conn.commit()
            return ("Teacher deleted successfully")
        else:
            return("Record not found")