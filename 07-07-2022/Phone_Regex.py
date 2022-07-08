# Validate Indian Phone Number

import re

mob = "+91 12345 67890"
reg = "[+0-9 0-9]+ [0-9]{5}$"
mobile_res = re.match(reg, mob)

if mobile_res:
    print(True)
else:
    print(False)
