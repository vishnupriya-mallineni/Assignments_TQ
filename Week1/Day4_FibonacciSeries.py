n = int(input())  # input indicates how many numbers we need in the sequence
a = 0     # Fibonacci seq starts with 0 and 1 initially
b = 1

# Running for loop to add the previous two numbers in the seq to get the next number
for i in range(n):
    print(a, end = " ")     #Returning each value in the seq
    a, b = b, a+b           # Modifying the numbers so that the seq goes on by adding the previous two numbers until for loop ends
    
