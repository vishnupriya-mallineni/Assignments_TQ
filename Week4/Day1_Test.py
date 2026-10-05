import pandas as pd
import matplotlib.pyplot as plt

Employees = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emily", "Stella"],
    "Department" : ["IT", "HR", "Sales", "IT", "HR", "IT"],
    "Age": [25, 35, 28, 44, 52, 32],
    "Salary": [10000, 16000, 14000, 25000, 45000, 12000]
}
df = pd.DataFrame(Employees)
print(df)

df.groupby("Department")["Name"].count().plot(kind="bar")
plt.title("Department Count")
plt.xlabel("Department")
plt.ylabel("Count")
plt.show()

df.groupby("Department")["Salary"].mean().plot(kind="hist")
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

plt.scatter(df["Age"], df["Salary"])
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()

