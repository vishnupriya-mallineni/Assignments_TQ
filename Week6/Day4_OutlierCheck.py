import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

data = {
    "Hours_Studied": [2, 3, 4, 5, 6, 4, 5, 7, 3, 6, 20],
    "Marks": [35, 40, 45, 50, 55, 48, 52, 60, 42, 58, 99]
}

df = pd.DataFrame(data)

X = df[["Hours_Studied", "Marks"]]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

center = np.median(X_scaled, axis=0)

distances = np.sqrt(
    np.sum((X_scaled - center) ** 2, axis=1)
)

df["Distance"] = distances

Q1 = df["Distance"].quantile(0.25)
Q3 = df["Distance"].quantile(0.75)

IQR = Q3 - Q1
threshold = Q3 + 1.5 * IQR

df["Outlier"] = df["Distance"] > threshold

print("Dataset with Distances:")
print(df.round(2))

print("\nDistance Threshold:", round(threshold, 2))

print("\nDetected Outliers:")
print(df[df["Outlier"]])

normal = df[~df["Outlier"]]
outliers = df[df["Outlier"]]

plt.figure(figsize=(8, 5))

plt.scatter(
    normal["Hours_Studied"],
    normal["Marks"],
    color="blue",
    s=100,
    label="Normal Points"
)

plt.scatter(
    outliers["Hours_Studied"],
    outliers["Marks"],
    color="red",
    marker="X",
    s=180,
    label="Outliers"
)

plt.title("Distance-Based Outlier Detection")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

df.to_csv("distance_outliers.csv", index=False)
