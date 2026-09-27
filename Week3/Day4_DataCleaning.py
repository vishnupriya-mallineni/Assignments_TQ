import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Alice", "Charlie", "David", "Bob"],
    "Department": ["IT", "HR", "IT", "sales", "SALES", "HR"],
    "Salary": ["45000", "50000", "45000", "55000", "60000", "50000"]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

print("\nDuplicate Rows:")
print(df[df.duplicated()])

df = df.drop_duplicates()

df.columns = df.columns.str.lower()
df["name"] = df["name"].str.strip().str.title()
df["department"] = df["department"].str.strip().str.upper()
df["salary"] = pd.to_numeric(df["salary"])

print("\nCleaned Data:")
print(df)

print("\nData Types:")
print(df.dtypes)
