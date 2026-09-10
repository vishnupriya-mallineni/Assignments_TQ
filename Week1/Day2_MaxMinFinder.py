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

