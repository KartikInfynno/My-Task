# Task - Pyhton
# There are x number of girls and they rolled a dice in turns one after another.

# If the number on the dice is , then the dice will be rolled again until she get a number other than .

# Since you know the sequence of numbers which the dice shows when rolled each time,
# you have to find what is the total number of girls or if the sequence is invalid.

# Input format
# A single line that contains a string denoting the sequence of numbers the dice rolls on written as string.

# Output format
# If the sequence is valid print the number of girls
# If the sequence is invalid print -1

# Sample Input
# 3662123

# Sample Output
# 5

def dice(inp):
    max_num = 6
    count = 0
    for i in range(len(inp)):
        if int(inp[i]) <= max_num:
            if int(inp[i]) != max_num:
                count += 1
            else:
                return -1
        else:
            return -1
    return count


inp = "3662123"
# int(inp[1])
dice(inp)
