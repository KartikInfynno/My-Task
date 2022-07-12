import re

re_hello = r"(.*hello)"
string = "my name is hello halo haelo hello"
m = re.match(re_hello, string)

if m:
    print("Valid")

else:
    print("Invalid")
