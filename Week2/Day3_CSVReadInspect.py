import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 72, 90, 68, 95]
}

df = pd.DataFrame(data)

df.to_csv("students.csv", index=False)

df = pd.read_csv("students.csv")

print("First 2 Rows:")
print(df.head(2))

print("\nLast 2 Rows:")
print(df.tail(2))

print("\nDataFrame Info:")
df.info()

print("\nStatistics:")
print(df.describe())
