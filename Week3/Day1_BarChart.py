import matplotlib.pyplot as plt

subjects = ["Math", "Science", "English", "History", "Computer"]
marks = [85, 78, 90, 72, 95]

plt.bar(subjects, marks)

plt.title("Student Marks by Subject")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.tight_layout()
plt.show()
