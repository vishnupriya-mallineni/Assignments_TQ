import numpy as np
import pandas as pd

marks = np.array([85, 72, 90, 68, 95])

print("Array:")
print(marks)

print("\nMean:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard Deviation:", np.std(marks))

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 72, 90, 68, 95]
}

df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)

print("\nStudents with Marks Above 80:")
print(df[df["Marks"] > 80])

print("\nStudents Age 20:")
print(df[df["Age"] == 20])

print("\nName and Marks:")
print(df[["Name", "Marks"]])

print("\nDataFrame Statistics:")
print(df.describe())

print("\nAverage Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())
