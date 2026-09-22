import pandas as pd
import numpy as np

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma", "Frank"],
    "Math": [85, 72, 90, np.nan, 95, 78],
    "Science": [80, 75, 88, 70, np.nan, 82],
    "English": [78, 68, 85, 65, 90, 76]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

df["Math"] = df["Math"].fillna(df["Math"].mean())
df["Science"] = df["Science"].fillna(df["Science"].mean())

df["Total"] = df["Math"] + df["Science"] + df["English"]
df["Average"] = df["Total"] / 3

print("\nCleaned Dataset:")
print(df)

print("\nDataset Statistics:")
print(df.describe())

print("\nHighest Average:")
print(df.loc[df["Average"].idxmax(), ["Name", "Average"]])

print("\nLowest Average:")
print(df.loc[df["Average"].idxmin(), ["Name", "Average"]])

print("\nClass Average:")
print(df["Average"].mean())

print("\nSummary:")
print("Number of Students:", len(df))
print("Highest Average:", df["Average"].max())
print("Lowest Average:", df["Average"].min())
print("Overall Class Average:", df["Average"].mean())

df.to_csv("cleaned_student_marks.csv", index=False)
