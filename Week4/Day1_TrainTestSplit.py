import pandas as pd
from sklearn.model_selection import train_test_split

data = {
    "Hours_Studied": [2, 3, 4, 5, 6, 7, 8, 9, 4, 6],
    "Attendance": [60, 65, 70, 75, 80, 85, 90, 95, 72, 88],
    "Previous_Marks": [50, 55, 60, 65, 70, 75, 80, 85, 62, 78],
    "Final_Marks": [52, 58, 63, 68, 74, 79, 84, 90, 65, 81]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

X = df[["Hours_Studied", "Attendance", "Previous_Marks"]]
y = df["Final_Marks"]

print("\nFeatures:")
print(X)

print("\nTarget:")
print(y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nX Train:")
print(X_train)

print("\nX Test:")
print(X_test)

print("\ny Train:")
print(y_train)

print("\ny Test:")
print(y_test)

print("\nTraining Size:", len(X_train))
print("Testing Size:", len(X_test))
