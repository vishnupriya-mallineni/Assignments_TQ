import pandas as pd
import numpy as np

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Age": [20, np.nan, 19, 22, np.nan],
    "Marks": [85, 72, np.nan, 68, 95]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nMissing Values:")
print(df.isnull())

print("\nMissing Value Count:")
print(df.isnull().sum())

filled_df = df.fillna(0)

print("\nAfter Filling Missing Values:")
print(filled_df)

dropped_df = df.dropna()

print("\nAfter Dropping Missing Values:")
print(dropped_df)
