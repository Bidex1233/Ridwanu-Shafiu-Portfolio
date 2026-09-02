import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("student_performance.csv")

# Basic information
print("STUDENT PERFORMANCE DATA")
print(df)

print("\nDATASET INFORMATION")
print(df.info())

print("\nSUMMARY STATISTICS")
print(df.describe())

# Average exam score
print("\nAVERAGE EXAM SCORE")
print(df["Exam_Score"].mean())

# Department performance
print("\nAVERAGE EXAM SCORE BY DEPARTMENT")
department_performance = df.groupby("Department")["Exam_Score"].mean()
print(department_performance)

# Best department
best_department = department_performance.idxmax()
best_score = department_performance.max()

print("\nBEST PERFORMING DEPARTMENT")
print(f"{best_department}: {best_score:.1f}")

# Pass/Fail
df["Result"] = df["Exam_Score"].apply(
    lambda score: "Pass" if score >= 50 else "Fail"
)

print("\nPASS/FAIL DISTRIBUTION")
print(df["Result"].value_counts())

# Study hours
print("\nAVERAGE STUDY HOURS")
print(df["Study_Hours"].mean())

# Correlations
print("\nCORRELATION BETWEEN STUDY HOURS AND EXAM SCORE")
print(df["Study_Hours"].corr(df["Exam_Score"]))

print("\nCORRELATION BETWEEN ATTENDANCE AND EXAM SCORE")
print(df["Attendance"].corr(df["Exam_Score"]))

# Chart 1: Department performance
department_performance.plot(
    kind="bar",
    title="Average Exam Score by Department"
)

plt.xlabel("Department")
plt.ylabel("Average Exam Score")
plt.tight_layout()
plt.savefig("department_performance.png")
plt.close()

# Chart 2: Attendance vs Exam Score
plt.scatter(df["Attendance"], df["Exam_Score"])

plt.title("Attendance vs Exam Score")
plt.xlabel("Attendance (%)")
plt.ylabel("Exam Score")
plt.tight_layout()
plt.savefig("attendance_vs_exam_score.png")
plt.close()

print("\nCHARTS SAVED SUCCESSFULLY")
highest_student = df.loc[df["Exam_Score"].idxmax()]
lowest_student = df.loc[df["Exam_Score"].idxmin()]

print("\nHIGHEST EXAM SCORE")
print(highest_student[["Student_ID", "Department", "Exam_Score"]])

print("\nLOWEST EXAM SCORE")
print(lowest_student[["Student_ID", "Department", "Exam_Score"]])
students_needing_attention = df[df["Exam_Score"] < 70]

print("\nSTUDENTS NEEDING ATTENTION")
print(
    students_needing_attention[
        ["Student_ID", "Department", "Attendance", "Study_Hours", "Exam_Score"]
    ]
)
attention_count = len(students_needing_attention)
attention_percentage = (attention_count / len(df)) * 100

print("\nSTUDENTS NEEDING ATTENTION")
print(f"{attention_count} out of {len(df)} students")

print("\nPERCENTAGE NEEDING ATTENTION")
print(f"{attention_percentage:.1f}%")