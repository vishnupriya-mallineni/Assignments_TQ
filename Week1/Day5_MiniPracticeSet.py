print("=== Problem 1: Student Grade Calculator ===")

marks = []

for i in range(5):
    mark = float(input(f"Enter mark {i + 1}: "))
    marks.append(mark)

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

print(f"Marks: {marks}")
print(f"Average: {average:.2f}")
print(f"Grade: {grade}")


print("\n=== Problem 2: Even and Odd Counter ===")

def count_even_odd(numbers):
    even = 0
    odd = 0

    for number in numbers:
        if number % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd


numbers = [10, 15, 22, 33, 40, 51]

even_count, odd_count = count_even_odd(numbers)

print("Numbers:", numbers)
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)


print("\n=== Problem 3: Student Records ===")

students = {
    "Alice": 85,
    "Bob": 55,
    "Charlie": 72,
    "David": 45,
    "Emma": 91
}

with open("student_results.txt", "w", encoding="utf-8") as file:
    for name, mark in students.items():
        if mark >= 60:
            result = "Pass"
        else:
            result = "Fail"

        file.write(f"{name}: {mark} - {result}\n")

with open("student_results.txt", "r", encoding="utf-8") as file:
    print(file.read())

