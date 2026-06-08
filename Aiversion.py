import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate data
marks = np.random.randint(0, 101, size=(50,5))

names = np.array([f"student_{i}" for i in range(1,51)])

attendance = np.random.randint(60,101,size=50)
study_hours = np.random.randint(1,41,size=50)

# Create DataFrame
df = pd.DataFrame({
    'Names': names,
    'Subject1': marks[:,0],
    'Subject2': marks[:,1],
    'Subject3': marks[:,2],
    'Subject4': marks[:,3],
    'Subject5': marks[:,4],
    'Attendance(%)': attendance,
    'Study_Hours': study_hours
})

subjects = ['Subject1','Subject2','Subject3','Subject4','Subject5']

df['Total'] = df[subjects].sum(axis=1)
df['Average'] = df[subjects].mean(axis=1)

print(df.head())
def assign_grade(avg):
    if avg >= 80:
        return 'A'
    elif avg >= 60:
        return 'B'
    elif avg >= 40:
        return 'C'
    elif avg >= 30:
        return 'D'
    else:
        return 'F'

df['Grade'] = df['Average'].apply(assign_grade)
print(df[['Names', 'Average', 'Grade']])
print(df.head())

fig, axes = plt.subplots(2, 3, figsize=(18,10))

# 1. Subject Averages
subject_avg = df[subjects].mean()

axes[0,0].bar(subject_avg.index, subject_avg.values)
axes[0,0].set_title("Subject Averages")

# 2. Grade Distribution
grade_counts = df['Grade'].value_counts()

axes[0,1].pie(
    grade_counts.values,
    labels=grade_counts.index,
    autopct='%1.1f%%'
)
axes[0,1].set_title("Grade Distribution")

# 3. Average Marks Distribution
axes[0,2].hist(df['Average'], bins=10)
axes[0,2].set_title("Average Marks Distribution")

# 4. Study Hours vs Average Marks
axes[1,0].scatter(
    df['Study_Hours'],
    df['Average']
)
axes[1,0].set_title("Study Hours vs Average Marks")
axes[1,0].set_xlabel("Study Hours")
axes[1,0].set_ylabel("Average Marks")

# 5. Attendance by Grade
attendance_grade = df.groupby('Grade')['Attendance(%)'].mean()

axes[1,1].bar(
    attendance_grade.index,
    attendance_grade.values
)
axes[1,1].set_title("Average Attendance by Grade")

# 6. Subject Score Comparison
axes[1,2].boxplot(
    [df[sub] for sub in subjects],
    tick_labels=subjects
)
axes[1,2].set_title("Subject Score Comparison")
plt.savefig("Student_dashboard.png",
            bbox_inches = 'tight')
plt.tight_layout()
plt.show()
df.to_csv("student_raw_data.csv", index=False)
df = pd.read_csv("student_raw_data.csv")
df.loc[5, 'Attendance(%)'] = np.nan
df.loc[10, 'Subject1'] = np.nan
df.loc[15, 'Study_Hours'] = np.nan
df.to_excel("student_data.xlsx", index=False)