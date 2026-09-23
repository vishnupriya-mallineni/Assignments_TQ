import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
sales = [100, 150, 120, 180, 200]
profit = [30, 45, 35, 60, 75]

plt.figure(figsize=(9, 5))

plt.plot(days, sales, marker="o", label="Sales")
plt.plot(days, profit, marker="s", label="Profit")

plt.title("Weekly Sales and Profit")
plt.xlabel("Days")
plt.ylabel("Amount")

plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()
