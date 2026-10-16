import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Hours_Studied": [2, 3, 4, 5, 6, 4, 5, 7, 3, 6, 20],
    "Marks": [35, 40, 45, 50, 55, 48, 52, 60, 42, 58, 99]
}

df = pd.DataFrame(data)

columns = ["Hours_Studied", "Marks"]

lower_bounds = {}
upper_bounds = {}

for column in columns:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_bounds[column] = Q1 - 1.5 * IQR
    upper_bounds[column] = Q3 + 1.5 * IQR

outlier_mask = pd.Series(False, index=df.index)

for column in columns:
    outlier_mask |= (
        (df[column] < lower_bounds[column]) |
        (df[column] > upper_bounds[column])
    )

df_removed = df.loc[~outlier_mask].copy()

df_capped = df.copy()

for column in columns:
    df_capped[column] = df_capped[column].clip(
        lower=lower_bounds[column],
        upper=upper_bounds[column]
    )

print("Original Dataset:")
print(df)

print("\nDetected Outliers:")
print(df[outlier_mask])

print("\nDataset After Removing Outliers:")
print(df_removed)

print("\nDataset After Capping Outliers:")
print(df_capped)

comparison = pd.DataFrame({
    "Original": [
        len(df),
        df["Hours_Studied"].mean(),
        df["Marks"].mean()
    ],
    "Removed": [
        len(df_removed),
        df_removed["Hours_Studied"].mean(),
        df_removed["Marks"].mean()
    ],
    "Capped": [
        len(df_capped),
        df_capped["Hours_Studied"].mean(),
        df_capped["Marks"].mean()
    ]
}, index=[
    "Number of Students",
    "Average Study Hours",
    "Average Marks"
])

print("\nComparison of Results:")
print(comparison.round(2))

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

datasets = [
    ("Original Data", df),
    ("Outliers Removed", df_removed),
    ("Outliers Capped", df_capped)
]

for ax, (title, dataset) in zip(axes, datasets):
    ax.scatter(
        dataset["Hours_Studied"],
        dataset["Marks"],
        s=100
    )

    ax.set_title(title)
    ax.set_xlabel("Hours Studied")
    ax.set_ylabel("Marks")
    ax.grid(True)

plt.tight_layout()
plt.show()

comparison.to_csv("outlier_comparison.csv")
