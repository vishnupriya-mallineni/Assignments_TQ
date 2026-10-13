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

centers = scaler.inverse_transform(model.cluster_centers_)

plt.figure(figsize=(8, 5))

for cluster in sorted(df["Cluster"].unique()):
    cluster_data = df[df["Cluster"] == cluster]

    plt.scatter(
        cluster_data["Hours_Studied"],
        cluster_data["Marks"],
        s=100,
        label=f"Cluster {cluster}"
    )

plt.scatter(
    centers[:, 0],
    centers[:, 1],
    c="red",
    marker="X",
    s=250,
    edgecolors="black",
    label="Cluster Centers"
)

plt.title("K-Means Clustering Visualization")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

print("Cluster Assignments:")
print(df)
