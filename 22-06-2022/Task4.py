# Task 4. Check is given number is Armstrong?
def armstrong(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        return f"{num} is an Armstrong number"
    else:
        return f"{num} is not an Armstrong number"


num = int(input("Enter a number: "))
armstrong(num)
