import sqlite3

class StudentModel:
    def __init__(self, db_name="student_info.db"):
        self.db_name = db_name
        self.init_db()

    def get_connection(self):
        return sqlite3.connect(self.db_name)

    def init_db(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    roll_no INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    department TEXT NOT NULL,
                    cgpa REAL NOT NULL
                )
            """)
            conn.commit()

    def add_student(self, roll_no, name, department, cgpa):
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO students (roll_no, name, department, cgpa) VALUES (?, ?, ?, ?)",
                    (roll_no, name, department, cgpa)
                )
                conn.commit()
                return True, f"Student '{name}' added successfully."
        except sqlite3.IntegrityError:
            return False, f"Error: Roll number {roll_no} already exists."

    def get_student_by_roll(self, roll_no):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students WHERE roll_no = ?", (roll_no,))
            return cursor.fetchone()

    def get_all_students(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students")
            return cursor.fetchall()