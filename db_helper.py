import mysql.connector

class DBHelper:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",        # MySQL server address
                user="root",             # your MySQL username
                password="F4d220190@", # your MySQL password
                database="student_management"   # your database name
            )
            self.cursor = self.conn.cursor(dictionary=True)
            print("✅ Connected to MySQL database successfully!")
        except mysql.connector.Error as err:
            print(f"❌ Database Connection Error: {err}")

    def fetch_all(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def execute(self, query, values=None):
        self.cursor.execute(query, values)
        self.conn.commit()
        return self.cursor.lastrowid

    def close(self):
        self.cursor.close()
        self.conn.close()