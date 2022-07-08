# Validate Mail Address

import re

st = "temp.123abc@gmail.com"

res = re.match("[a-z0-9._+-]+@[a-zA-Z]+.[a-zA-z0-9]{2,}$", st)

if res:
    print(True)
else:
    print(False)
