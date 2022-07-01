# Check if Brackets Are Perfectly Closed or Not


equation = "{1-(2+4)/}[4*{5-6]}"
open_li = ["{", "(", "["]
close_li = ["}", ")", "]"]
check_li = []

for i in equation:
    if i in open_li:
        check_li.append(i)

    elif i in close_li:
        p = close_li.index(i)
        if len(check_li) > 0 and open_li[p] == check_li[-1]:
            check_li.pop()
        else:
            check_li.append(i)


if len(check_li) == 0:
    print("Valid")
else:
    print("invalid")
