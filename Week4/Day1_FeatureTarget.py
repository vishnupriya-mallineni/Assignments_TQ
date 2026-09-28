import pandas as pd

data = {
    "Hours_Studied": [2, 3, 4, 5, 6, 7, 8, 9],
    "Attendance": [60, 65, 70, 75, 80, 85, 90, 95],
    "Previous_Marks": [50, 55, 60, 65, 70, 75, 80, 85],
    "Final_Marks": [52, 58, 63, 68, 74, 79, 84, 90]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

X = df[["Hours_Studied", "Attendance", "Previous_Marks"]]
y = df["Final_Marks"]

print("\nIndependent Variables (Features):")
print(X)

print("\nDependent Variable (Target):")
print(y)

print("\nFeature Names:")
print(X.columns.tolist())

print("\nTarget Name:")
print(y.name)
