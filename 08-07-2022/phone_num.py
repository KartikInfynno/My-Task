import re

string = "898-898-8988"
re_phone = '[0-9]{3}\-[0-9]{3}\-[0-9]{4}'
check = re.match(re_phone, string)

if check:
    print("valid")
else:
    print("Invalid")
