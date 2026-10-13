import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = {
    "Hours_Studied": [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 9, 10],
    "Marks": [30, 35, 40, 45, 50, 55, 65, 70, 80, 85, 90, 95]
}

df = pd.DataFrame(data)

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

df["Cluster"] = model.fit_predict(scaled_data)

print("Clustered Dataset:")
print(df)

print("\nStudents in Each Cluster:")
print(df["Cluster"].value_counts().sort_index())

print("\nAverage Values by Cluster:")
print(df.groupby("Cluster")[["Hours_Studied", "Marks"]].mean())

plt.scatter(
    df["Hours_Studied"],
    df["Marks"],
    c=df["Cluster"],
    cmap="viridis",
    s=100
)

plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.title("Student Groups Using K-Means Clustering")
plt.colorbar(label="Cluster")
plt.grid(True)
plt.tight_layout()
plt.show()
