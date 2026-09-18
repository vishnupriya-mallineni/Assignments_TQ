import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 72, 90, 68, 95]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

df = df.rename(columns={
    "Name": "Student_Name",
    "Marks": "Score"
})

print("\nRenamed Columns:")
print(df)

sorted_score = df.sort_values(by="Score", ascending=False)

print("\nSorted by Score:")
print(sorted_score)

sorted_multiple = df.sort_values(
    by=["Age", "Score"],
    ascending=[True, False]
)

print("\nSorted by Age and Score:")
print(sorted_multiple)
