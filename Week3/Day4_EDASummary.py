import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Henry"],
    "Department": ["IT", "HR", "IT", "Sales", "HR", "IT", "Sales", "HR"],
    "Age": [22, 25, 28, 30, 32, 35, 38, 40],
    "Salary": [42000, 45000, 50000, 55000, 58000, 65000, 70000, 75000],
    "Performance": [68, 72, 75, 78, 82, 85, 88, 92]
}

df = pd.DataFrame(data)

department_counts = df["Department"].value_counts()

department_counts.plot(kind="bar")
plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.show()

average_salary = df.groupby("Department")["Salary"].mean()

average_salary.plot(kind="bar")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.tight_layout()
plt.show()

plt.scatter(df["Age"], df["Salary"])
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.scatter(df["Age"], df["Performance"])
plt.title("Age vs Performance")
plt.xlabel("Age")
plt.ylabel("Performance")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.hist(df["Salary"], bins=5, edgecolor="black")
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
