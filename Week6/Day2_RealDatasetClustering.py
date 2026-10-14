import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

print("Original Dataset:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

X = df[["petal length (cm)", "petal width (cm)"]]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

df["Cluster"] = model.fit_predict(X_scaled)

print("\nCluster Assignments:")
print(df.head(15))

print("\nNumber of Flowers in Each Cluster:")
print(df["Cluster"].value_counts().sort_index())

print("\nCluster Summary:")
print(
    df.groupby("Cluster")[
        ["petal length (cm)", "petal width (cm)"]
    ].mean().round(2)
)

score = silhouette_score(X_scaled, df["Cluster"])

print("\nSilhouette Score:", round(score, 3))

centers = scaler.inverse_transform(model.cluster_centers_)

plt.figure(figsize=(8, 5))

for cluster in sorted(df["Cluster"].unique()):
    group = df[df["Cluster"] == cluster]

    plt.scatter(
        group["petal length (cm)"],
        group["petal width (cm)"],
        label=f"Cluster {cluster}",
        s=60
    )

plt.scatter(
    centers[:, 0],
    centers[:, 1],
    c="red",
    marker="X",
    s=250,
    label="Cluster Centers"
)

plt.title("K-Means Clustering on Iris Dataset")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

df.to_csv("clustered_iris.csv", index=False)
