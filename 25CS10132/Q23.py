import xml.etree.ElementTree as ET
from xml.dom import minidom

class StudentXMLManager:
    def __init__(self, filename="students.xml"):
        self.filename = filename

    def create_database(self):
        """Initializes a new XML document with the root element <Students>."""
        root = ET.Element("Students")
        tree = ET.ElementTree(root)
        self._save_tree(tree)
        print(f"Database initialized: {self.filename}")

    def add_student(self, student_id, name, age, course, grade):
        """Adds a new student element with child tags and attributes."""
        try:
            tree = ET.parse(self.filename)
            root = tree.getroot()
        except FileNotFoundError:
            root = ET.Element("Students")
            tree = ET.ElementTree(root)

        
        for student in root.findall("Student"):
            if student.get("id") == student_id:
                print(f"Error: Student ID {student_id} already exists.")
                return
 
        student_elem = ET.SubElement(root, "Student", attrib={"id": student_id})
        
        ET.SubElement(student_elem, "Name").text = name
        ET.SubElement(student_elem, "Age").text = str(age)
        ET.SubElement(student_elem, "Course").text = course
        ET.SubElement(student_elem, "Grade").text = grade

        self._save_tree(tree)
        print(f"Success: Student '{name}' added.")

    def update_grade(self, student_id, new_grade):
        """Modifies an existing student's grade based on their ID."""
        try:
            tree = ET.parse(self.filename)
            root = tree.getroot()
        except FileNotFoundError:
            print("Database file not found.")
            return

        updated = False
        for student in root.findall("Student"):
            if student.get("id") == student_id:
                grade_elem = student.find("Grade")
                if grade_elem is not None:
                    grade_elem.text = new_grade
                    updated = True

        if updated:
            self._save_tree(tree)
            print(f"Success: Grade updated for Student ID {student_id}.")
        else:
            print(f"Error: Student ID {student_id} not found.")

    def display_students(self):
        """Parses and displays all student records stored in the XML."""
        try:
            tree = ET.parse(self.filename)
            root = tree.getroot()
            print("\n--- Current Student Records ---")
            for student in root.findall("Student"):
                s_id = student.get("id")
                name = student.find("Name").text
                age = student.find("Age").text
                course = student.find("Course").text
                grade = student.find("Grade").text
                print(f"ID: {s_id} | Name: {name} | Age: {age} | Course: {course} | Grade: {grade}")
            print("-------------------------------\n")
        except FileNotFoundError:
            print("Database file not found.")

    def _save_tree(self, tree):
        """Helper method to format and save the XML tree cleanly."""
        rough_string = ET.tostring(tree.getroot(), 'utf-8')
        reparsed = minidom.parseString(rough_string)
        pretty_xml = reparsed.toprettyxml(indent="  ")
        with open(self.filename, "w", encoding="utf-8") as f:
            f.write(pretty_xml)


if __name__ == "__main__":
    manager = StudentXMLManager("students.xml")

    
    manager.create_database()

    manager.add_student("S001", "Alice Smith", 20, "Computer Science", "A")
    manager.add_student("S002", "Bob Jones", 22, "Mathematics", "B+")

    
    manager.display_students()

    
    manager.update_grade("S002", "A-")

   
    manager.display_students()