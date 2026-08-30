import pandas as pd

data = {
    "ID": [101, 102, 103, 104, 105, 106,107, 108,],
    "Name": ["Aisha", "Musa", "John", "Fatima", "David", "Musa", "Ibrahim", "Grace"],
    "Age": [19, 20, None, 21, 19, 20, 22, None,],
    "Department": [
      "Meteorology",
      "Computer science",
      "Cyber security",
      "computer science",
      "Meteorology",
      "Computer science", 
      "cybersecurity", 
      "Meteorology"
    ],
    "Score": [78, 85, 72, 91, None, 85, 67,88],
}
df = pd.DataFrame(data)

print(df)

print(df.isnull().sum())
print(df.duplicated(subset=["Name","Age", "Department", "Score"]))
df = df.drop_duplicates(
    subset=["Name", "Age", "Department", "Score"], 
                        keep="first"
)
print(df)
#print(df["Department"].unique())
df["Department"] = df["Department"].replace({"computer science": "Computer science",
                         "Cyber security": "cybersecurity"
})
print(df["Department"].unique())
median_age = df["Age"].median()
print(median_age)
df["Age"] = df["Age"].fillna(median_age)
print(df)
print(df.isnull().sum())
print(df[df["Score"].isnull()])

df.to_csv("cleaned_student_data.csv",
index=False)
print("Dataset saved successfully!")