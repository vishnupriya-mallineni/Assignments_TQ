import pandas as pd

marks = pd.Series(
    [85, 72, 90, 68, 95],
    index=["Alice", "Bob", "Charlie", "David", "Emma"]
)

print("Student Marks:")
print(marks)

print("\nFirst Value:")
print(marks.iloc[0])

print("\nAlice's Mark:")
print(marks["Alice"])

print("\nFirst Three Students:")
print(marks.iloc[0:3])

print("\nMarks Greater Than 80:")
print(marks[marks > 80])

print("\nAll Values:")
print(marks.values)
