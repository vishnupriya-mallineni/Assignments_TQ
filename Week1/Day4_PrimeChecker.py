def is_prime(number):
    c=0
    for i in range(1, number+1):
        if number % i == 0:
            c+=1
    if c == 2:
        return "Is a prime number"
    else:
        return "Is not a prime number"
        
print(is_prime(int(input())))
