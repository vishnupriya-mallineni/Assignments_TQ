import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 72, 90, 68, 95]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nSingle Column:")
print(df["Name"])

print("\nMultiple Columns:")
print(df[["Name", "Marks"]])

print("\nStudents with Marks Greater Than 80:")
print(df[df["Marks"] > 80])

print("\nStudents Age 20:")
print(df[df["Age"] == 20])

print("\nStudents with Marks Greater Than 80 and Age 20:")
print(df[(df["Marks"] > 80) & (df["Age"] == 20)])
