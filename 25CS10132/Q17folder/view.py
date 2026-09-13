class EmployeeView:
    @staticmethod
    def show_menu():
        print("\n--- Employee CRUD Operations ---")
        print("1. Create (Add Employee)")
        print("2. Read (View All Employees)")
        print("3. Update (Modify Employee)")
        print("4. Delete (Remove Employee)")
        print("5. Exit")
        return input("Enter choice (1-5): ")

    @staticmethod
    def get_employee_input():
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Name: ")
        designation = input("Enter Designation: ")
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))
        return emp_id, name, designation, department, salary

    @staticmethod
    def get_update_input():
        emp_id = int(input("Enter Employee ID to update: "))
        print("Leave input blank to keep existing value.")
        designation = input("Enter New Designation: ") or None
        department = input("Enter New Department: ") or None
        sal_input = input("Enter New Salary: ")
        salary = float(sal_input) if sal_input else None
        return emp_id, designation, department, salary

    @staticmethod
    def get_employee_id_input(action_name):
        return int(input(f"Enter Employee ID to {action_name}: "))

    @staticmethod
    def display_message(message):
        print(message)

    @staticmethod
    def display_all_employees(employees):
        if not employees:
            print("No employee records found.")
            return

        print("\n--- Employee Records ---")
        print(f"{'ID':<6} {'Name':<18} {'Designation':<20} {'Department':<15} {'Salary':<10}")
        print("-" * 70)
        for row in employees:
            print(f"{row[0]:<6} {row[1]:<18} {row[2]:<20} {row[3]:<15} {row[4]:<10.2f}")