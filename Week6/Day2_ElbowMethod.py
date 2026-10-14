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

k_values = range(1, 11)
inertia_values = []

for k in k_values:
    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    model.fit(X_scaled)
    inertia_values.append(model.inertia_)

    print("K:", k, "Inertia:", round(model.inertia_, 3))

plt.figure(figsize=(8, 5))
plt.plot(k_values, inertia_values, marker="o")

plt.title("Elbow Method for K-Means")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia (WCSS)")
plt.xticks(list(k_values))
plt.grid(True)
plt.tight_layout()
plt.show()

best_k = 3

final_model = KMeans(
    n_clusters=best_k,
    random_state=42,
    n_init=10
)

df["Cluster"] = final_model.fit_predict(X_scaled)

print("\nFinal Cluster Assignments:")
print(df)

print("\nCluster Averages:")
print(df.groupby("Cluster")[["Hours_Studied", "Marks"]].mean())
