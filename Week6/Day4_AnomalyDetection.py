import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Student": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"],
    "Hours_Studied": [2, 3, 4, 5, 6, 4, 5, 7, 3, 6, 5, 20],
    "Marks": [35, 40, 45, 50, 55, 48, 52, 60, 42, 58, 54, 99]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

columns = ["Hours_Studied", "Marks"]

outlier_mask = pd.Series(False, index=df.index)

for column in columns:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    column_outliers = (
        (df[column] < lower_bound) |
        (df[column] > upper_bound)
    )

    outlier_mask = outlier_mask | column_outliers

    print(f"\n{column}")
    print("Lower Bound:", round(lower_bound, 2))
    print("Upper Bound:", round(upper_bound, 2))
    print("Outliers:")
    print(df.loc[column_outliers, ["Student", column]])

df["Outlier"] = outlier_mask

print("\nDataset with Outlier Labels:")
print(df)

print("\nDetected Outliers:")
print(df[df["Outlier"]])

plt.figure(figsize=(8, 5))

plt.boxplot(
    [df["Hours_Studied"], df["Marks"]],
    tick_labels=["Hours Studied", "Marks"]
)

plt.title("Outlier Detection Using IQR")
plt.ylabel("Values")
plt.grid(True)
plt.tight_layout()
plt.show()

df.to_csv("outlier_results.csv", index=False)
