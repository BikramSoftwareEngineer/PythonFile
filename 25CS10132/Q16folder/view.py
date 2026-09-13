class StudentView:
    @staticmethod
    def show_menu():
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Search Student by Roll No")
        print("3. Display All Students")
        print("4. Exit")
        return input("Enter your choice (1-4): ")

    @staticmethod
    def get_student_input():
        roll_no = int(input("Enter Roll Number: "))
        name = input("Enter Name: ")
        department = input("Enter Department: ")
        cgpa = float(input("Enter CGPA: "))
        return roll_no, name, department, cgpa

    @staticmethod
    def get_roll_no_input():
        return int(input("Enter Roll Number to search: "))

    @staticmethod
    def display_message(message):
        print(message)

    @staticmethod
    def display_student_details(student):
        if student:
            print("\n--- Student Details ---")
            print(f"Roll No    : {student[0]}")
            print(f"Name       : {student[1]}")
            print(f"Department : {student[2]}")
            print(f"CGPA       : {student[3]}")
        else:
            print("Student not found.")

    @staticmethod
    def display_all_students(students):
        if not students:
            print("No student records available.")
            return
        
        print("\n--- All Student Records ---")
        print(f"{'Roll No':<10} {'Name':<20} {'Department':<15} {'CGPA':<5}")
        print("-" * 55)
        for row in students:
            print(f"{row[0]:<10} {row[1]:<20} {row[2]:<15} {row[3]:<5}")