import re

us_zip = "1234-12345"

re_us = "^[0-9]{4}(-[0-9]{5})$"

res_us_zip = re.match(re_us, us_zip)

if res_us_zip:
    print(True)
else:
    print(False)
