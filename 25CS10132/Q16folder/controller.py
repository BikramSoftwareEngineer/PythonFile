from models import StudentModel
from view import StudentView

class StudentController:
    def __init__(self):
        self.model = StudentModel()
        self.view = StudentView()

    def run(self):
        while True:
            choice = self.view.show_menu()

            if choice == '1':
                try:
                    roll, name, dept, cgpa = self.view.get_student_input()
                    success, message = self.model.add_student(roll, name, dept, cgpa)
                    self.view.display_message(message)
                except ValueError:
                    self.view.display_message("Invalid input. Please enter numbers for Roll No and CGPA.")

            elif choice == '2':
                try:
                    roll = self.view.get_roll_no_input()
                    student = self.model.get_student_by_roll(roll)
                    self.view.display_student_details(student)
                except ValueError:
                    self.view.display_message("Invalid Roll Number.")

            elif choice == '3':
                students = self.model.get_all_students()
                self.view.display_all_students(students)

            elif choice == '4':
                self.view.display_message("Exiting system. Goodbye!")
                break
            else:
                self.view.display_message("Invalid choice. Please try again.")