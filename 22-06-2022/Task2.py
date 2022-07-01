# Task 2. Check is given string list is Fibonacci or not?

def fibonacci(num):
    a = 0
    b = 1
    while b < num:
        c = a+b
        a = b
        b = c
    if b == num or a == num:
        return True
    if b > num:
        return False


num = int(input("Enter a number to check"))
if fibonacci(num):
    print(f"{num} is a fibonacci number.")
else:
    print(f"{num} is not a fibonacci number.")
