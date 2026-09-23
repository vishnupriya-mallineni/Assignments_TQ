import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Age": [22, 25, 28, 32, 35, 40, 45],
    "Salary": [35000, 42000, 48000, 55000, 62000, 75000, 82000]
}

df = pd.DataFrame(data)

plt.scatter(df["Age"], df["Salary"])

plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")

plt.grid(True)
plt.tight_layout()
plt.show()
