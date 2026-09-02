# Student Performance Analysis

## Project Overview

This project analyzes student academic performance using Python and Pandas.

The dataset contains information about students' departments, study hours, attendance, test scores, and examination scores.

## Objectives

The project aims to:

- Analyze overall student performance.
- Compare performance across departments.
- Examine the relationship between study hours and exam scores.
- Examine the relationship between attendance and exam scores.
- Identify students who may require additional academic attention.
- Visualize important findings.

## Tools Used

- Python
- Pandas
- Matplotlib
- CSV
- Visual Studio Code

## Dataset

The dataset contains 15 student records with the following variables:

- Student ID
- Age
- Department
- Gender
- Study Hours
- Attendance
- Test Score
- Exam Score

## Key Findings

- The average exam score was **79.4/100**.
- **Computer Science** had the highest average exam score at **86.4/100**.
- The dataset recorded a **100% pass rate** using a pass threshold of 50.
- Students studied an average of approximately **7.07 hours**.
- Study hours and exam score had a strong positive correlation of approximately **0.95**.
- Attendance and exam score had a very strong positive correlation of approximately **0.98**.
- **3 out of 15 students (20%)** scored below 70 and were flagged for further attention.
- The highest exam score was **95**, while the lowest was **59**.

## Visualizations

The project generates two visualizations:

### Average Exam Score by Department

`department_performance.png`

This chart compares the average examination performance of the three departments.

### Attendance vs Exam Score

`attendance_vs_exam_score.png`

This scatter plot visualizes the relationship between attendance and examination performance.

## Important Note

The correlations identified in this project describe relationships within this dataset. They do not prove that study hours or attendance alone cause higher examination scores.

The dataset is also relatively small, containing only 15 students, so the findings should not be generalized to a larger population without additional data.

## Skills Demonstrated

- Python programming
- Pandas
- Data analysis
- Data visualization
- Correlation analysis
- Grouped analysis
- Dataset interpretation
- Critical thinking

## Project Structure

```text
04_Student_Performance_Analysis/
│
├── student_performance.csv
├── performance_analysis.py
├── department_performance.png
├── attendance_vs_exam_score.png
└── README.md