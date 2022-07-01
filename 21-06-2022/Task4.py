# 4. Match with partner number => In list I'm 4 then match my partner. 8, 16, 24,44, etc are my partner number.
me = int(input("Enter Your Number"))
partners = []

my_p = []

for i in range(0, 5):
    val = int(input())

    partners.append(val)

for i in partners:
    if i % me == 0:
        my_p.append(i)

if len(my_p) == 0:
    print("Partners Not Found")
else:
    print(f"My Partners are {my_p}")
