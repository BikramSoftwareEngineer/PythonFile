import os

# Step 1: Creating a sample input text file for demonstration purposes
input_filename = "student_marks.txt"
output_filename = "student_results.txt"

sample_input_data = """RollNo,Name,Maths,Physics,Chemistry,English
101,Aarav Sharma,85,90,78,88
102,Priya Verma,92,88,95,90
103,Rahul Gupta,65,70,68,72
104,Ananya Iyer,78,82,80,85
105,Vikram Singh,55,60,58,62
"""

with open(input_filename, "w") as f:
    f.write(sample_input_data.strip())

# Step 2: Helper function to assign grades based on average marks
def determine_grade(average):
    if average >= 90:
        return 'A+'
    elif average >= 80:
        return 'A'
    elif average >= 70:
        return 'B'
    elif average >= 60:
        return 'C'
    elif average >= 50:
        return 'D'
    else:
        return 'F'

# Step 3: Read from input file, process records, and write results to output file
processed_records = []

with open(input_filename, "r") as infile:
    lines = infile.readlines()
    
    # Process each student record (skipping the header)
    for line in lines[1:]:
        if not line.strip():
            continue
        
        # Parse comma-separated values
        parts = [p.strip() for p in line.split(',')]
        roll_no = parts[0]
        name = parts[1]
        marks = [float(m) for m in parts[2:]]
        
        # Calculations
        total_marks = sum(marks)
        average_marks = total_marks / len(marks)
        grade = determine_grade(average_marks)
        
        # Store formatted result
        processed_records.append(f"{roll_no},{name},{total_marks},{average_marks:.2f},{grade}\n")

# Step 4: Write the calculated results to the output file
with open(output_filename, "w") as outfile:
    outfile.write("RollNo,Name,TotalMarks,AverageMarks,Grade\n")
    outfile.writelines(processed_records)

print("Processing complete!")
print(f"Results successfully written to '{output_filename}'.")

# Optional: Display content of the generated output file
print("\n--- Contents of Output File ---")
with open(output_filename, "r") as outfile:
    print(outfile.read())