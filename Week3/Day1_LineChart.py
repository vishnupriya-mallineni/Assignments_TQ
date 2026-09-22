import matplotlib.pyplot as plt

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
marks = [70, 75, 80, 78, 90]

plt.plot(days, marks, marker="o")

plt.title("Student Marks During the Week")
plt.xlabel("Days")
plt.ylabel("Marks")

plt.grid(True)
plt.tight_layout()

plt.show()
