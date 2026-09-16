import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 72, 90, 68, 95]
}

df1 = pd.DataFrame(data)

print("DataFrame from Dictionary:")
print(df1)

students = [
    ["Alice", 20, 85],
    ["Bob", 21, 72],
    ["Charlie", 19, 90],
    ["David", 22, 68],
    ["Emma", 20, 95]
]

df2 = pd.DataFrame(students, columns=["Name", "Age", "Marks"])

print("\nDataFrame from List:")
print(df2)

print("\nFirst Two Rows:")
print(df2.head(2))

print("\nLast Two Rows:")
print(df2.tail(2))

print("\nColumns:")
print(df2.columns)

print("\nName Column:")
print(df2["Name"])

print("\nFirst Row:")
print(df2.iloc[0])
