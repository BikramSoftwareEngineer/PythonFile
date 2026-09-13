from models import EmployeeModel
from view import EmployeeView

class EmployeeController:
    def __init__(self):
        self.model = EmployeeModel()
        self.view = EmployeeView()

    def run(self):
        while True:
            choice = self.view.show_menu()

            if choice == '1':
                try:
                    emp_id, name, desig, dept, sal = self.view.get_employee_input()
                    success, message = self.model.create_employee(emp_id, name, desig, dept, sal)
                    self.view.display_message(message)
                except ValueError:
                    self.view.display_message("Invalid input. Please enter numbers for ID and Salary.")

            elif choice == '2':
                employees = self.model.get_all_employees()
                self.view.display_all_employees(employees)

            elif choice == '3':
                try:
                    emp_id, desig, dept, sal = self.view.get_update_input()
                    success, message = self.model.update_employee(emp_id, desig, dept, sal)
                    self.view.display_message(message)
                except ValueError:
                    self.view.display_message("Invalid numerical value entered.")

            elif choice == '4':
                try:
                    emp_id = self.view.get_employee_id_input("delete")
                    success, message = self.model.delete_employee(emp_id)
                    self.view.display_message(message)
                except ValueError:
                    self.view.display_message("Invalid Employee ID.")

            elif choice == '5':
                self.view.display_message("Exiting system. Goodbye!")
                break
            else:
                self.view.display_message("Invalid choice. Please try again.")