import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Department": ["IT", "HR", "IT", "Sales", "HR", "IT", "Sales", "HR"],
    "Salary": [45000, 50000, 48000, 60000, 55000, 52000, 65000, 58000]
}

df = pd.DataFrame(data)

department_counts = df["Department"].value_counts()

print("Employee Count by Department:")
print(department_counts)

department_counts.plot(kind="bar")
plt.title("Employee Count by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.show()

average_salary = df.groupby("Department")["Salary"].mean()

print("\nAverage Salary by Department:")
print(average_salary)

average_salary.plot(kind="bar")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.tight_layout()
plt.show()
