import re

string = 'I like coffee but I always date to tea.'
check_i = re.findall('I', string)


if check_i:
    print("Valid")
else:
    print("Invalid")

print("length = ", len(check_i))
