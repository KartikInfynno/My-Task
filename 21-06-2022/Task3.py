# 3. Odd out / Even out
li3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_li = []
even_li = []

for i in li3:
    if i % 2 == 0:
        even_li.append(i)
    else:
        odd_li.append(i)

print(f"Even List {even_li}\nOdd List: {odd_li}")
