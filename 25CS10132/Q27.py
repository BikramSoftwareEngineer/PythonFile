import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 1. Load the student examination data
data = {
    "Student": [
        "S1",
        "S2",
        "S3",
        "S4",
        "S5",
        "S6",
        "S7",
        "S8",
        "S9",
        "S10",
    ],
    "Mathematics": [78, 85, 67, 90, 73, 81, 69, 94, 76, 88],
    "Physics": [72, 88, 70, 92, 75, 79, 68, 90, 74, 85],
    "Chemistry": [75, 82, 65, 88, 78, 83, 72, 92, 79, 86],
    "English": [80, 84, 72, 91, 76, 80, 70, 95, 77, 89],
}

df = pd.DataFrame(data)

# Set the visual style of Seaborn
sns.set_theme(style="whitegrid")

# 2. Subject-wise Score Distributions (Boxplot / Histplot)
plt.figure(figsize=(10, 6))
sns.boxplot(data=df.drop(columns=["Student"]), palette="Set2")
plt.title("Subject-wise Score Distributions")
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.show()

# 3. Pairwise Relationships (Pairplot)
sns.pairplot(df.drop(columns=["Student"]), diag_kind="kde", palette="husl")
plt.suptitle("Pairwise Relationships Between Subjects", y=1.02)
plt.show()

# 4. Correlation Heatmap
plt.figure(figsize=(8, 6))
correlation_matrix = df.drop(columns=["Student"]).corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap of Subjects")
plt.show()