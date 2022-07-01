#      1
#     2 4
#    3 5 7
#   6 8 10 12
#  9 11 13 15 17
# 14 16 18 20 22 24

# Pattern
n = 6
j = 1
li = 0
for col in range(n):
    for space in range(n - col - 1):
        print(' ', end='')
    if col % 2 == 0:
        for row in range(1 * col + 1):
            print(j, end=" ")
            j = j + 2
    else:
        for i in range(n):
            for k in range(1 * col + 1):
                li += 2
                print(li, end=' ')
            break
    print()
