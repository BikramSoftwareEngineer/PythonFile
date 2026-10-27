class StudentRecordManager:
    def __init__(self):
        # Using a list of dictionaries to store student records
        self.students = []

    def insert_student(self, roll_no, name, age, course):
        # Check if student with same roll number already exists
        for student in self.students:
            if student["roll_no"] == roll_no:
                print(f"Error: Student with Roll Number {roll_no} already exists.")
                return
        
        student_record = {
            "roll_no": roll_no,
            "name": name,
            "age": age,
            "course": course
        }
        self.students.append(student_record)
        print(f"Student '{name}' added successfully.")

    def delete_student(self, roll_no):
        for student in self.students:
            if student["roll_no"] == roll_no:
                self.students.remove(student)
                print(f"Student with Roll Number {roll_no} deleted successfully.")
                return
        print(f"Error: Student with Roll Number {roll_no} not found.")

    def search_student(self, roll_no):
        for student in self.students:
            if student["roll_no"] == roll_no:
                print("\nStudent Found:")
                print(f"Roll Number : {student['roll_no']}")
                print(f"Name        : {student['name']}")
                print(f"Age         : {student['age']}")
                print(f"Course      : {student['course']}")
                return student
        print(f"Error: Student with Roll Number {roll_no} not found.")
        return None

    def display_all(self):
        if not self.students:
            print("No student records available.")
            return
        
        print("\n--- All Student Records ---")
        for student in self.students:
            print(f"Roll No: {student['roll_no']} | Name: {student['name']} | Age: {student['age']} | Course: {student['course']}")
        print("-" * 30)


# Driver Code / Demonstration
manager = StudentRecordManager()

# Insertion
manager.insert_student(101, "Aarav Sharma", 20, "Computer Science")
manager.insert_student(102, "Priya Verma", 21, "Electronics")
manager.insert_student(103, "Rahul Gupta", 19, "Mechanical")

# Display all records
manager.display_all()

# Search operation
print("\nSearching for Roll Number 102:")
manager.search_student(102)

# Deletion operation
print("\nDeleting Roll Number 103:")
manager.delete_student(103)

# Display all records after deletion
manager.display_all()