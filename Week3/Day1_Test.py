import numpy as np
import pandas as pd

Students = {
     "Name" : ["Alice", "Bob", "Charlie" ], 
    "Marks": [15, 25,35]
}
df = pd.DataFrame(Students)
print(df)

print("\n", np.mean(df["Marks"]))
print("\n", np.min(df["Marks"]))
print("\n", np.max(df["Marks"]))

print("\n", df.describe())

print("\n", df["Marks"]>= 20)










