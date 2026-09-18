import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma", "Frank"],
    "Department": ["IT", "HR", "IT", "HR", "Sales", "Sales"],
    "Marks": [85, 72, 90, 68, 95, 80]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

count = df.groupby("Department")["Name"].count()

print("\nStudent Count by Department:")
print(count)

average = df.groupby("Department")["Marks"].mean()

print("\nAverage Marks by Department:")
print(average)
