import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Age": [22, 25, 28, 32, 35, 40],
    "Experience": [1, 3, 5, 7, 10, 15],
    "Salary": [35000, 42000, 48000, 55000, 62000, 75000],
    "Performance": [65, 70, 75, 80, 85, 90]
}

df = pd.DataFrame(data)

correlation_matrix = df.corr()

print("Correlation Matrix:")
print(correlation_matrix)

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f")

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()
