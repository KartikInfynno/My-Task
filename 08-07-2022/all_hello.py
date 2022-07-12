import re

string = 'hello my name is hello halo haelo hello'
check_i = re.findall('hello', string)


if check_i:
    print("Valid")
else:
    print("Invalid")

print("length = ", len(check_i))
