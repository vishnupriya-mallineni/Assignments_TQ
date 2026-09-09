print("\n==========LIST OPERATIONS ==========")

numbers = [30, 10, 50, 20, 40]
print("Original List:")
print(numbers)


# Append
numbers.append(60)
print("\nAfter append(60):")
print(numbers)


# Insert
numbers.insert(2, 25)
print("\nAfter insert(2, 25):")
print(numbers)

# Remove
numbers.remove(10)
print("\nAfter remove(10):")
print(numbers)

# Sort
numbers.sort()
print("\nAfter sort():")
print(numbers)

# Reverse
numbers.reverse()
print("\nAfter reverse():")
print(numbers)


print("\n==========Max and Min ==========")

numbers = [45, 12, 89, 23, 7, 67, 34]

maximum = numbers[0]
minimum = numbers[0]
for number in numbers:
    if number > maximum:
        maximum = number
    if number < minimum:
        minimum = number


print("Numbers:", numbers)
print("Maximum number:",maximum)
print("Minimum number:", minimum)

print("\n====== SUM AND AVERAGE ==========")


def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total

def calculate_average(numbers):
    total = calculate_sum(numbers)
    average = total / len(numbers)
    return average


numbers = [10, 20, 30, 40, 50]
total = calculate_sum(numbers)
average = calculate_average(numbers)
print("Numbers:", numbers)
print("Sum:", total)
print("Average:", average)


print("\n======== MULTIPLICATION TABLE ==========")

number = int(input("Enter a number: "))
print("\nMultiplication Table of", number)
for i in range(1, 11):
    result = number * i
    print(number, "x", i, "=", result)

