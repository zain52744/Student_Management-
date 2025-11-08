from db_helper import DBHelper

class ScoreModel:
    def __init__(self):
        self.db = DBHelper()

    def add_score(self, stu_id,subj_id,marks,grades):
        query = "INSERT INTO scores(stu_id,subj_id,marks,grades) VALUES (%s,%s,%s,%s)"
        self.db.cursor.execute(query,(stu_id,subj_id,marks,grades,))
        self.db.conn.commit()
        return("Scores added successfully")
    
    def get_all_scores(self):
        query =  "SELECT * FROM scores"
        self.db.cursor.execute(query,)
        return self.db.cursor.fetchall()
    
    def get_score_by_id(self, sco_id):
        query = "SELECT * FROM scores WHERE sco_id = %s"
        self.db.cursor.execute(query,(sco_id,))
        return self.db.cursor.fetchone()
    
    def update_score_by_id(self, sco_id,stu_id,subj_id,marks,grades):
        query = "SELECT * FROM scores WHERE sco_id=%s"
        self.db.cursor.execute(query,(sco_id,))
        score = self.db.cursor.fetchone()

        if score:
            update_query = """
            UPDATE scores SET stu_id=%s, subj_id=%s, marks=%s, grades=%s
            WHERE sco_id = %s
"""         
            self.db.cursor.execute(update_query,(stu_id,subj_id,marks,grades,sco_id,))
            self.db.conn.commit()
            return("Score updated successfully")
        else:
            return("Record not found")
            
    def delete_score_by_id(self, sco_id):
        query = "SELECT * FROM scores WHERE sco_id = %s"
        self.db.cursor.execute(query,(sco_id,))
        score = self.db.cursor.fetchone()

        if score:
            delete_query = "DELETE FROM scores WHERE sco_id=%s"
            self.db.cursor.execute(delete_query,(sco_id,))
            self.db.conn.commit()
            return("Score deleted successfully")
        else:
            return("Record not found")