import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score, adjusted_rand_score

data = {
    "Hours_Studied": [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 9, 10],
    "Marks": [30, 35, 40, 45, 50, 55, 65, 70, 80, 85, 90, 95]
}

df = pd.DataFrame(data)

X = df[["Hours_Studied", "Marks"]]

model_before = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

df["Before_Scaling"] = model_before.fit_predict(X)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model_after = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

df["After_Scaling"] = model_after.fit_predict(X_scaled)

print("Cluster Assignments:")
print(df)

print("\nBefore Scaling - Cluster Averages:")
print(df.groupby("Before_Scaling")[["Hours_Studied", "Marks"]].mean())

print("\nAfter Scaling - Cluster Averages:")
print(df.groupby("After_Scaling")[["Hours_Studied", "Marks"]].mean())

print("\nSilhouette Score Before Scaling:")
print(silhouette_score(X, df["Before_Scaling"]))

print("\nSilhouette Score After Scaling:")
print(silhouette_score(X_scaled, df["After_Scaling"]))

print("\nAdjusted Rand Index Between Clusterings:")
print(adjusted_rand_score(
    df["Before_Scaling"],
    df["After_Scaling"]
))

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].scatter(
    df["Hours_Studied"],
    df["Marks"],
    c=df["Before_Scaling"],
    cmap="viridis",
    s=100
)

axes[0].set_title("Before Feature Scaling")
axes[0].set_xlabel("Hours Studied")
axes[0].set_ylabel("Marks")
axes[0].grid(True)

axes[1].scatter(
    df["Hours_Studied"],
    df["Marks"],
    c=df["After_Scaling"],
    cmap="viridis",
    s=100
)

axes[1].set_title("After Feature Scaling")
axes[1].set_xlabel("Hours Studied")
axes[1].set_ylabel("Marks")
axes[1].grid(True)

plt.tight_layout()
plt.show()

df.to_csv("scaling_comparison.csv", index=False)
