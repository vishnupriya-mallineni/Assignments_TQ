import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
sales = [100, 150, 120, 180, 200]

plt.figure(figsize=(8, 5))
plt.plot(days, sales, marker="o", label="Sales")
plt.title("Weekly Sales")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("weekly_sales.png")
plt.show()

subjects = ["Math", "Science", "English", "Computer"]
marks = [85, 78, 90, 95]

plt.figure(figsize=(8, 5))
plt.bar(subjects, marks, label="Marks")
plt.title("Subject Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.legend()
plt.grid(axis="y")
plt.tight_layout()

plt.savefig("subject_marks.png")
plt.show()
