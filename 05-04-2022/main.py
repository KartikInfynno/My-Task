import json
import module

f = open('data.json')
data = json.load(f)

# type(data)
for i in range(0, len(data["data"])):
    data['data'][i]["Age"] = module.find_age(data['data'][i]["DOB"])

# print(data["data"])
print(type(data["data"][i]))

for i in range(0, len(data["data"])):
    for k, v in data["data"][i].items():
        print(k, " : ", v)
