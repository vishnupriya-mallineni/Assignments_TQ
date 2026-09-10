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
