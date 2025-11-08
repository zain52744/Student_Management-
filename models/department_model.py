from db_helper import DBHelper

class DepartmentModel:
    def __init__(self):
        self.db = DBHelper()

    
    def add_department(self, dept_name):
        query = "INSERT INTO department(dept_name) VALUES (%s)" 
        self.db.cursor.execute(query,(dept_name,))
        self.db.conn.commit()
        return("Department added successfully")
    
    def get_all_department(self):
        query = "SELECT * FROM department"
        self.db.cursor.execute(query,)
        return self.db.cursor.fetchall()
    
    def get_department_by_id(self, dept_id):
        query = "SELECT * FROM department WHERE dept_id = %s"
        self.db.cursor.execute(query,(dept_id,))
        return self.db.cursor.fetchone()
    
    def update_department_by_id(self, dept_id,dept_name):
        query = "SELECT * FROM department WHERE dept_id = %s"
        self.db.cursor.execute(query,(dept_id,))
        department = self.db.cursor.fetchone()

        if department:
            update_query = "UPDATE department SET dept_name = %s WHERE dept_id = %s"
            self.db.cursor.execute(update_query,(dept_name,dept_id,))
            self.db.conn.commit()
            return ("Department updated successfully")
        else:
            return ("Department not found")

    def delete_department_by_id(self, dept_id):
        query = "SELECT * FROM department WHERE dept_id = %s"
        self.db.cursor.execute(query,(dept_id,))
        department = self.db.cursor.fetchone()

        if department:
            delete_query = "DELETE FROM department WHERE dept_id = %s"
            self.db.cursor.execute(delete_query,(dept_id,))
            self.db.conn.commit()
            return ("Department deleted successfully")
        else:
            return ("Department not found")
