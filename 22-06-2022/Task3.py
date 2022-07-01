# Task 3. Find the Prime number from given string list.
import sympy


def is_prime(num):
    prime = sympy.isprime(num)
    if prime == True:
        print(f"{num} is prime number")
    else:
        print(f"{num} is not a prime number")


num = int(input("enter number to check: "))
is_prime(num)
