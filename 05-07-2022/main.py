import json
import module

f = open('data.json')
data = json.load(f)
for i in range(0, len(data["data"])):
    data['data'][i]["Age"] = module.find_age(data['data'][i]["DOB"])

d = [data["data"][i:i+5] for i in range(0, len(data["data"]), 5)]

count = 0

string = "P , " + " , ".join([str(i+1) for i in range(len(d))]) + " , N"

c = 0


def pageing(c):
    # c = 0
    #     c +=5
    for i in data["data"][c:c+5]:
        for k, v in i.items():
            if k:
                if k == "DOB":
                    print(k, " : ", module.date_format(v))
                else:
                    print(k, " : ", v)

        print()
    return


for i in data["data"][:5]:
    for k, v in i.items():
        if k:
            if k == "DOB":
                print(k, " : ", module.date_format(v))
            else:
                print(k, " : ", v)
    print()

while True:

    inp = input(string)
    print()
    if inp == "n" or inp == "N":
        c += 5
        pageing(c)
        if c == 25:
            print("End of the Page")

    elif inp == "p" or inp == "P":
        c -= 5
        pageing(c)
        if c < 0:
            print("No Page Left")

    elif inp == "1":
        for i in data["data"][:5]:
            for k, v in i.items():
                if k:
                    if k == "DOB":
                        print(k, " : ", module.date_format(v))
                    else:
                        print(k, " : ", v)
            print()
        # c = c + 5

    elif inp == "2":
        for i in data["data"][5:10]:
            for k, v in i.items():
                if k:
                    if k == "DOB":
                        print(k, " : ", module.date_format(v))
                    else:
                        print(k, " : ", v)
            print()
        c = c + 5

    elif inp == "3":
        for i in data["data"][10:15]:
            for k, v in i.items():
                if k:
                    if k == "DOB":
                        print(k, " : ", module.date_format(v))
                    else:
                        print(k, " : ", v)
            print()
        c = c + 5

    elif inp == "4":
        for i in data["data"][15:20]:
            for k, v in i.items():
                if k:
                    if k == "DOB":
                        print(k, " : ", module.date_format(v))
                    else:
                        print(k, " : ", v)
            print()
        # c = 20
        c = c + 5

    elif inp == "5":
        for i in data["data"][20:25]:
            for k, v in i.items():
                if k:
                    if k == "DOB":
                        print(k, " : ", module.date_format(v))
                    else:
                        print(k, " : ", v)
            print()
        c = c + 5

    else:
        print("Invalid Input")
