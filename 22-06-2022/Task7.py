#     1
#    A E
#   2 3 4
#  I O U A
# 5 6 7 8 9

# Pattern

n = int(input("Enter number of rows: "))
j = 1
li = ["A", "E", "I", "O", "U"]
count = 0

for col in range(n):
    for space in range(n - col - 1):
        print(' ', end='')
    if col % 2 == 0:
        for row in range(1 * col + 1):
            print(j, end=" ")
            j = j + 1
    else:
        for i in range(len(li) - count):
            for k in range(1 * col + 1):
                print(li[count], end=' ')
                count = count + 1
                if count == 5:
                    count = 0
            break
    print()
