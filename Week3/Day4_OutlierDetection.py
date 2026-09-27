import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Salary": [35000, 38000, 40000, 42000, 45000, 48000, 50000, 52000, 55000, 120000]
}

df = pd.DataFrame(data)

plt.figure(figsize=(8, 5))
plt.boxplot(df["Salary"])
plt.title("Salary Box Plot")
plt.ylabel("Salary")
plt.grid(True)
plt.tight_layout()
plt.show()

Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[
    (df["Salary"] < lower_bound) |
    (df["Salary"] > upper_bound)
]

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

print("\nOutliers:")
print(outliers)
