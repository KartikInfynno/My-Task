import re

ind_zip = "123456"

re_zip = "^[0-9]{6}$"

res_zip = re.match(re_zip, ind_zip)

if res_zip:
    print(True)
else:
    print(False)
