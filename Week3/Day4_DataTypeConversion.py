import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": ["22", "25", "28", "30"],
    "Salary": ["45000", "50000", "55000", "60000"],
    "Join_Date": ["2024-01-15", "2023-06-20", "2022-09-10", "2024-03-05"],
    "Department": ["IT", "HR", "Sales", "IT"]
}

df = pd.DataFrame(data)

print("Original Data Types:")
print(df.dtypes)

df["Age"] = pd.to_numeric(df["Age"])
df["Salary"] = pd.to_numeric(df["Salary"])
df["Join_Date"] = pd.to_datetime(df["Join_Date"])
df["Department"] = df["Department"].astype("category")

print("\nConverted Data:")
print(df)

print("\nNew Data Types:")
print(df.dtypes)
