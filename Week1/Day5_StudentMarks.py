students = {
    "Alice": [85, 90, 78],
    "Bob": [72, 68, 75],
    "Charlie": [95, 92, 88],
    "David": [60, 65, 58],
    "Emma": [45, 50, 48]
}

for name, marks in students.items():
    average = sum(marks) / len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"Student: {name}")
    print(f"Marks: {marks}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")
    
