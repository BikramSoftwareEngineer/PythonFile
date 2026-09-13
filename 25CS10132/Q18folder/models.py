import sqlite3

class ReportModel:
    def __init__(self, db_name="company.db"):
        self.db_name = db_name
        self.init_db()

    def get_connection(self):
        return sqlite3.connect(self.db_name)

    def init_db(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS employees (
                    emp_id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    designation TEXT NOT NULL,
                    department TEXT NOT NULL,
                    salary REAL NOT NULL
                )
            """)
            
            cursor.execute("SELECT COUNT(*) FROM employees")
            if cursor.fetchone()[0] == 0:
                sample_employees = [
                    (101, "Alice", "Developer", "IT", 75000.00),
                    (102, "Bob", "Manager", "IT", 95000.00),
                    (103, "Charlie", "Recruiter", "HR", 50000.00),
                    (104, "Diana", "HR Lead", "HR", 68000.00),
                    (105, "Evan", "Analyst", "Finance", 70000.00),
                    (106, "Fiona", "Accountant", "Finance", 62000.00)
                ]
                cursor.executemany(
                    "INSERT INTO employees VALUES (?, ?, ?, ?, ?)", sample_employees
                )
                conn.commit()

    def get_department_employees(self, department):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            query = "SELECT emp_id, name, designation, salary FROM employees WHERE department = ?"
            cursor.execute(query, (department,))
            return cursor.fetchall()

    def get_department_summary(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            query = """
                SELECT department, 
                       COUNT(emp_id) as total_employees, 
                       SUM(salary) as total_salary, 
                       AVG(salary) as avg_salary 
                FROM employees 
                GROUP BY department
            """
            cursor.execute(query)
            return cursor.fetchall()