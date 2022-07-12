import re


reg = "([0-2][0-5][0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.([0-2][0-5][0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.([0-2][0-5][0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.([0-2][0-5][0-5]|[0-2][0-4][0-9]|[01]?[0-9][0-9]?)$"
ip = input("Enter IP Address : ")
check = re.match(reg,ip)

if check:
    print("Valid IP Address")

else:
    print("Invalid IP Address")