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

print("Dataset with Cluster Labels:")
print(df)

cluster_summary = df.groupby("Cluster").agg(
    Student_Count=("Marks", "count"),
    Average_Hours=("Hours_Studied", "mean"),
    Average_Marks=("Marks", "mean"),
    Minimum_Marks=("Marks", "min"),
    Maximum_Marks=("Marks", "max")
)

print("\nCluster Summary:")
print(cluster_summary.round(2))

cluster_order = cluster_summary["Average_Marks"].sort_values().index

group_names = ["Lower Performance", "Medium Performance", "Higher Performance"]

cluster_names = dict(zip(cluster_order, group_names))

df["Cluster_Group"] = df["Cluster"].map(cluster_names)

print("\nDataset with Group Names:")
print(df)

for cluster in sorted(df["Cluster"].unique()):
    group = df[df["Cluster"] == cluster]

    print("\nCluster:", cluster)
    print("Group:", cluster_names[cluster])
    print("Students:", len(group))
    print("Average Study Hours:", round(group["Hours_Studied"].mean(), 2))
    print("Average Marks:", round(group["Marks"].mean(), 2))

df.to_csv("clustered_students.csv", index=False)

plt.figure(figsize=(8, 5))

for cluster in sorted(df["Cluster"].unique()):
    group = df[df["Cluster"] == cluster]

    plt.scatter(
        group["Hours_Studied"],
        group["Marks"],
        s=100,
        label=cluster_names[cluster]
    )

plt.title("Student Cluster Analysis")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
