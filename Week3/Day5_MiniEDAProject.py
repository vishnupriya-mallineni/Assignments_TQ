import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("student_data.csv")

print("First Five Rows:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

print("\nAverage Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())

print("\nAverage Marks by Department:")
print(df.groupby("Department")["Marks"].mean())

df["Department"].value_counts().plot(kind="bar")
plt.title("Students by Department")
plt.xlabel("Department")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.show()

plt.hist(df["Marks"], bins=5, edgecolor="black")
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

plt.scatter(df["Attendance"], df["Marks"])
plt.title("Attendance vs Marks")
plt.xlabel("Attendance")
plt.ylabel("Marks")
plt.grid(True)
plt.tight_layout()
plt.show()

numeric_df = df[["Age", "Marks", "Attendance"]]
correlation = numeric_df.corr()

plt.figure(figsize=(7, 5))
sns.heatmap(correlation, annot=True, fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

average_marks = df.groupby("Department")["Marks"].mean()

average_marks.plot(kind="bar")
plt.title("Average Marks by Department")
plt.xlabel("Department")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.show()
