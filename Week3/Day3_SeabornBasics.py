import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Henry"],
    "Department": ["IT", "HR", "IT", "Sales", "HR", "IT", "Sales", "HR"],
    "Age": [22, 25, 24, 30, 28, 26, 32, 29],
    "Salary": [45000, 50000, 48000, 60000, 55000, 52000, 65000, 58000],
    "Experience": [1, 3, 2, 6, 4, 3, 7, 5]
}

df = pd.DataFrame(data)

sns.countplot(x="Department", data=df)
plt.title("Employee Count by Department")
plt.xlabel("Department")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

sns.boxplot(x="Department", y="Salary", data=df)
plt.title("Salary Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.tight_layout()
plt.show()

sns.pairplot(df[["Age", "Salary", "Experience"]])
plt.show()
