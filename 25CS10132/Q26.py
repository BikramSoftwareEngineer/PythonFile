import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


data = {
    'Student': ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10'],
    'Study_Hours': [8, 10, 12, 15, 18, 20, 7, 14, 16, 22],
    'Exam_Score': [65, 72, 75, 82, 88, 90, 60, 80, 85, 95]
}

df = pd.DataFrame(data)


correlation = df['Study_Hours'].corr(df['Exam_Score'])
print(f"--- Analysis Summary ---")
print(f"Correlation coefficient between Study Hours and Exam Score: {correlation:.4f}\n")


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))


ax1.hist(df['Study_Hours'], bins=5, alpha=0.6, label='Study Hours/Week', color='royalblue', edgecolor='black')
ax1.set_title('Distribution of Study Hours')
ax1.set_xlabel('Hours per Week')
ax1.set_ylabel('Frequency')
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.legend()


sns.scatterplot(x='Study_Hours', y='Exam_Score', data=df, s=120, color='purple', ax=ax2, label='Students')
sns.regplot(x='Study_Hours', y='Exam_Score', data=df, scatter=False, color='crimson', ax=ax2, label='Trend Line')
ax2.set_title('Study Hours vs. Examination Score')
ax2.set_xlabel('Study Hours / Week')
ax2.set_ylabel('Exam Score')
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.legend()


plt.tight_layout()


plt.savefig('study_hours_vs_scores.png')
print("Visualizations saved successfully as 'study_hours_vs_scores.png'!")
plt.show()