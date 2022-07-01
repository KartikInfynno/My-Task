# 5. Palidrom string
string = input("Enter a string to check")

if string == string[::-1]:
    print(f"{string} is Palindrom")

else:
    print(f"{string} is Not Palindrom")
