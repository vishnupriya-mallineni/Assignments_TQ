import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Math": [85, 72, 90, 68, 95],
    "Science": [80, 75, 88, 70, 92],
    "English": [78, 68, 85, 65, 90]
}

df = pd.DataFrame(data)

df["Total"] = df["Math"] + df["Science"] + df["English"]

df["Percentage"] = df["Total"] / 300 * 100

print(df)
