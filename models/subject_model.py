from db_helper import DBHelper

class SubjectModel:
    def __init__(self):
        self.db = DBHelper()

    def add_subjects(self, stu_id,teach_id,cour_id,subj_name):
        query = "INSERT INTO subjects(stu_id,teach_id,cour_id,subj_name) VALUES (%s,%s,%s,%s)"
        self.db.cursor.execute(query,(stu_id,teach_id,cour_id,subj_name,))
        self.db.conn.commit()
        return("Subject added successfully")

    def get_all_subjects(self):
        query = "SELECT * FROM subjects"
        self.db.cursor.execute(query,)
        return self.db.cursor.fetchall()

    def get_subject_by_id(self, subj_id):
        query = "SELECT * FROM subjects WHERE subj_id = %s"
        self.db.cursor.execute(query,(subj_id,))
        return self.db.cursor.fetchone()
        
    def update_subject_by_id(self, subj_id,stu_id,teach_id,cour_id,subj_name):
        query = "SELECT * FROM subjects WHERE subj_id = %s"
        self.db.cursor.execute(query,(subj_id,))
        subject = self.db.cursor.fetchone()

        if subject:
            update_query = """
                UPDATE subjects SET stu_id=%s, teach_id=%s, cour_id=%s, subj_name=%s
                WHERE subj_id = %s
"""
            self.db.cursor.execute(update_query,(stu_id,teach_id,cour_id,subj_name,subj_id,))
            self.db.conn.commit()
            return("Subject updated successfully")
        else:
            return("Subject not found")
        
    def delete_subject_by_id(self, subj_id):
        query = "SELECT * FROM subjects WHERE subj_id = %s"
        self.db.cursor.execute(query,(subj_id,))
        subject = self.db.cursor.fetchone()

        if subject:
            delete_query = "DELETE FROM subjects WHERE subj_id = %s"
            self.db.cursor.execute(delete_query,(subj_id,))
            self.db.conn.commit()
            return("Subject deleted successfully")
        else:
            return("Subject not found")
        