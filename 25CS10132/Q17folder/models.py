import sqlite3

class EmployeeModel:
    def __init__(self, db_name="employee_management.db"):
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
            conn.commit()

    def create_employee(self, emp_id, name, designation, department, salary):
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO employees (emp_id, name, designation, department, salary) VALUES (?, ?, ?, ?, ?)",
                    (emp_id, name, designation, department, salary)
                )
                conn.commit()
                return True, f"Employee '{name}' added successfully."
        except sqlite3.IntegrityError:
            return False, f"Error: Employee ID {emp_id} already exists."

    def get_all_employees(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM employees")
            return cursor.fetchall()

    def get_employee_by_id(self, emp_id):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM employees WHERE emp_id = ?", (emp_id,))
            return cursor.fetchone()

    def update_employee(self, emp_id, designation, department, salary):
        employee = self.get_employee_by_id(emp_id)
        if not employee:
            return False, f"Error: No employee found with ID {emp_id}."

        desig = designation if designation else employee[2]
        dept = department if department else employee[3]
        sal = salary if salary is not None else employee[4]

        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE employees 
                SET designation = ?, department = ?, salary = ? 
                WHERE emp_id = ?
            """, (desig, dept, sal, emp_id))
            conn.commit()
            return True, f"Employee ID {emp_id} updated successfully."

    def delete_employee(self, emp_id):
        if not self.get_employee_by_id(emp_id):
            return False, f"Error: No employee found with ID {emp_id}."

        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM employees WHERE emp_id = ?", (emp_id,))
            conn.commit()
            return True, f"Employee ID {emp_id} deleted successfully."