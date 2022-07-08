import re

us_mobile = "+1 (202) 555-4111"

re_us_mobile = "^[+0-9]{2} [(0-9)]{5} [0-9]{3}[-][0-9]{4}$"

res_us_mobile = re.match(re_us_mobile, us_mobile)

if res_us_mobile:
    print(True)
else:
    print(False)
