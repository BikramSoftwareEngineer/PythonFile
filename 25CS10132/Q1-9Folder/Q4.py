# Using tuples to store immutable student details (Roll No, Name)
student1 = (101, "Aarav Sharma")
student2 = (102, "Priya Verma")
student3 = (103, "Rahul Gupta")
student4 = (104, "Ananya Iyer")
student5 = (105, "Vikram Singh")

# Sets representing course enrolments containing student identifiers/names
python_course = {student1[1], student2[1], student3[1], student4[1]}
data_science_course = {student2[1], student3[1], student5[1]}
web_dev_course = {student1[1], student4[1], student5[1]}

print("--- Course Enrolments ---")
print(f"Python Course Enrolled Students: {python_course}")
print(f"Data Science Course Enrolled Students: {data_science_course}")
print(f"Web Development Course Enrolled Students: {web_dev_course}")

# 1. Union: All unique students enrolled across all courses
all_enrolled_students = python_course.union(data_science_course, web_dev_course)
print(f"\nTotal Unique Students Enrolled (Union): {all_enrolled_students}")

# 2. Intersection: Students enrolled in both Python and Data Science
python_and_ds = python_course.intersection(data_science_course)
print(f"Students Enrolled in Both Python & Data Science (Intersection): {python_and_ds}")

# 3. Intersection across all three courses (Common to all)
common_to_all = python_course.intersection(data_science_course, web_dev_course)
print(f"Students Enrolled in All Three Courses: {common_to_all}")

# 4. Difference: Students enrolled in Python but NOT in Data Science
python_only = python_course.difference(data_science_course)
print(f"Students Enrolled in Python Only (Difference): {python_only}")

# 5. Symmetric Difference: Students enrolled in either Python or Data Science, but not both
symmetric_diff = python_course.symmetric_difference(data_science_course)
print(f"Students in Either Python or Data Science, but not both (Symmetric Difference): {symmetric_diff}")