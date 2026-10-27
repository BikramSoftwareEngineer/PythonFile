import numpy as np

# Data provided from the experiment document
# Subjects: Mathematics, Physics, Chemistry, English
# Students: S1, S2, S3, S4, S5

# Mid-Semester Examination Marks Matrix (5 students x 4 subjects)
mid_sem_marks = np.array([
    [65, 70, 68, 72],  # S1
    [78, 75, 80, 77],  # S2
    [55, 60, 58, 62],  # S3
    [82, 85, 80, 88],  # S4
    [70, 68, 72, 74]   # S5
])

# End-Semester Examination Marks Matrix (5 students x 4 subjects)
end_sem_marks = np.array([
    [72, 78, 75, 80],  # S1
    [84, 82, 86, 83],  # S2
    [65, 68, 66, 70],  # S3
    [88, 90, 85, 92],  # S4
    [78, 75, 80, 82]   # S5
])

students = ["S1", "S2", "S3", "S4", "S5"]
subjects = ["Mathematics", "Physics", "Chemistry", "English"]

# 1. Compute Total Marks using vectorized addition
mid_sem_total = np.sum(mid_sem_marks, axis=1)
end_sem_total = np.sum(end_sem_marks, axis=1)

# 2. Compute Average Marks across subjects (4 subjects)
mid_sem_avg = mid_sem_total / len(subjects)
end_sem_avg = end_sem_total / len(subjects)

# 3. Compute Percentage Improvement from Mid-Sem to End-Sem using vectorized operations
percentage_improvement = ((end_sem_total - mid_sem_total) / mid_sem_total) * 100

# Display Results
print("=" * 75)
print(f"{'Student':<10} | {'Mid-Sem Total':<15} | {'End-Sem Total':<15} | {'Improvement (%)':<15}")
print("=" * 75)

for i, student in enumerate(students):
    print(f"{student:<10} | {mid_sem_total[i]:<15.1f} | {end_sem_total[i]:<15.1f} | {percentage_improvement[i]:<15.2f}%")

print("=" * 75)

# Overall Class Statistics
overall_mid_avg = np.mean(mid_sem_avg)
overall_end_avg = np.mean(end_sem_avg)
print(f"\nClass Average (Mid-Sem): {overall_mid_avg:.2f}")
print(f"Class Average (End-Sem): {overall_end_avg:.2f}")