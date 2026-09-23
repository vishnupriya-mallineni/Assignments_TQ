import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
sales = [100, 150, 120, 180, 200]

plt.figure()
plt.plot(days, sales, marker="o")
plt.title("Daily Sales")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

subjects = ["Math", "Science", "English", "Computer"]
marks = [85, 78, 90, 95]

plt.figure()
plt.bar(subjects, marks)
plt.title("Marks by Subject")
plt.xlabel("Subject")
plt.ylabel("Marks")
plt.show()

ages = [22, 25, 28, 32, 35, 40]
salaries = [35000, 42000, 48000, 55000, 62000, 75000]

plt.figure()
plt.scatter(ages, salaries)
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.grid(True)
plt.show()
