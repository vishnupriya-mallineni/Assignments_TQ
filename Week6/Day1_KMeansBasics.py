import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = {
    "Hours_Studied": [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 9, 10],
    "Marks": [30, 35, 40, 45, 50, 55, 65, 70, 80, 85, 90, 95]
}

df = pd.DataFrame(data)

X = df[["Hours_Studied", "Marks"]]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

df["Cluster"] = model.fit_predict(X_scaled)

print("Cluster Assignments:")
print(df)

print("\nNumber of Students in Each Cluster:")
print(df["Cluster"].value_counts().sort_index())

print("\nCluster Averages:")
print(df.groupby("Cluster")[["Hours_Studied", "Marks"]].mean())

print("\nCluster Centers (Scaled):")
print(model.cluster_centers_)

plt.scatter(
    df["Hours_Studied"],
    df["Marks"],
    c=df["Cluster"],
    cmap="viridis",
    s=100
)

plt.title("K-Means Student Clustering")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.colorbar(label="Cluster")
plt.grid(True)
plt.tight_layout()
plt.show()
