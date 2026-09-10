number = int(input("Enter a number: "))
print("\nMultiplication Table of", number)
for i in range(1, 11):
    result = number * i
    print(number, "x", i, "=", result)
