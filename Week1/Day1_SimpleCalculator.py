print("Calculator Menu")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Choose an operation (1-4): "))


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if choice == 1:
    result = num1 + num2
    print("Answer:", result)
elif choice == 2:
    result = num1 - num2
    print("Answer:", result)
elif choice == 3:
    result = num1 * num2
    print("Answer:", result)
elif choice == 4:
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        result = num1 / num2
        print("Answer:", result)
else:
    print("Invalid choice. Please select 1, 2, 3, or 4.")
