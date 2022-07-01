string = "kartik"
dictionary = {}

for i in set(string):
    print(i)
    dictionary[i] = string.count(i)

print(dictionary)
