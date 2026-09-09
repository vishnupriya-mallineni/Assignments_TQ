print("===NUMBER CLASSIFICATION====")

number = int(input("Enter a number: "))
if number > 0:
    print(number, "is Positive")
elif number < 0:
    print(number, "is Negative")
else:
    print("The number is Zero")

print("\n ====EVEN / ODD CHECKER=== ")

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
print("Enter 5 numbers:")

for i in range(5):
    number = int(input("Enter number: "))
    result = check_even_odd(number)
    print(number, "is", result)
    
print("\n======= SIMPLE CALCULATOR ==========")

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
