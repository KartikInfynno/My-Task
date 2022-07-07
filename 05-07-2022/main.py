from audioop import reverse
import json

from sympy import true
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


def page(c):

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
        elif inp == "2":
            for i in data["data"][5:10]:
                for k, v in i.items():
                    if k:
                        if k == "DOB":
                            print(k, " : ", module.date_format(v))
                        else:
                            print(k, " : ", v)
                print()
            c = 10
        elif inp == "3":
            for i in data["data"][10:15]:
                for k, v in i.items():
                    if k:
                        if k == "DOB":
                            print(k, " : ", module.date_format(v))
                        else:
                            print(k, " : ", v)
                print()
            c = 15
        elif inp == "4":
            for i in data["data"][15:20]:
                for k, v in i.items():
                    if k:
                        if k == "DOB":
                            print(k, " : ", module.date_format(v))
                        else:
                            print(k, " : ", v)
                print()
            c = 20
        elif inp == "5":
            for i in data["data"][20:25]:
                for k, v in i.items():
                    if k:
                        if k == "DOB":
                            print(k, " : ", module.date_format(v))
                        else:
                            print(k, " : ", v)
                print()
            c = 25

        elif inp == "0":
            break

        else:
            print("Invalid Input")


def sort_Name_a():
    s_name = data["data"].copy()
    s_name.sort(key=module.filter_name)
    for i in s_name:
        for k, v in i.items():
            if k:
                if k == "DOB":
                    print(k, " : ", module.date_format(v))
                else:
                    print(k, " : ", v)
        print()
# def sort_Name_d():
#     s_name = data["data"].copy()
#     s_name.sort(key=module.filter_name, reverse=True)
#     for i in s_name:
#         for k, v in i.items():
#             if k:
#                 if k == "DOB":
#                     print(k, " : ", module.date_format(v))
#                 else:
#                     print(k, " : ", v)
#         print()


def sort_Age_a():
    s_Age = data["data"].copy()
    s_Age.sort(key=module.filter_age)
    for i in s_Age:
        for k, v in i.items():
            if k:
                if k == "DOB":
                    print(k, " : ", module.date_format(v))
                else:
                    print(k, " : ", v)
        print()
# def sort_Age_d():
#     s_name = data["data"].copy()
#     s_name.sort(key=module.filter_age, reverse=True)
#     for i in s_name:
#         for k, v in i.items():
#             if k:
#                 if k == "DOB":
#                     print(k, " : ", module.date_format(v))
#                 else:
#                     print(k, " : ", v)
#         print()


def sort_DOB_a():
    s_DOB = data["data"].copy()
    s_DOB.sort(key=module.filter_dob, reverse=True)
    for i in s_DOB:
        for k, v in i.items():
            if k:
                if k == "DOB":
                    print(k, " : ", module.date_format(v))
                else:
                    print(k, " : ", v)
        print()
# def sort_DOB_d():
#     s_name = data["data"].copy()
#     s_name.sort(key=module.filter_dob, reverse=True)
#     for i in s_name:
#         for k, v in i.items():
#             if k:
#                 if k == "DOB":
#                     print(k, " : ", module.date_format(v))
#                 else:
#                     print(k, " : ", v)
#         print()


while True:
    print("Press 1 for Paging")
    print("Press 2 for Sorting by name")
    print("Press 3 for Sorting by age")
    print("Press 4 for Sorting by DOB")
    print("Press 0 For Exit")

    inpu = input()

    if inpu == "1":
        page(c)

    elif inpu == "2":
        sort_Name_a()

    elif inpu == "3":
        sort_Age_a()

    elif inpu == "4":
        sort_DOB_a()

    elif inpu == "0":
        break
