import sympy

string = "1, 3, A, RAJ, AADI, $, A, E, I, O, U, 323, 4, 8, 10, 100, 1000, kartik"

li = string.split(", ")
digit_li = []
char_li = []
vowel_li = []
square_list = []
cube_list = []
same_latter = []
prime_li = []
unique_li = []
palindrome_li = []
double_li = []
str1 = ", "

for i in li:
    if i.isdigit():
        digit_li.append(int(i))
    else:
        char_li.append(i)


def is_double(char_li):
    for i in char_li:
        #     dictionary = {}
        for j in i:
            if i.count(j) > 1:
                double_li.append(i)
                break
    print(
        f"Double Possetion Words from the inserted String : {str1.join(double_li)}")


def is_vowel(char_li):

    vowels = 'aeiouAEIOU'
    count = 0

    for char in char_li:
        if char in vowels:
            count += 1
            vowel_li.append(str(char))

    print(f"Vowels From the inserted String : {str1.join(vowel_li)}")


def is_unique_element(li):

    vowels = '!@#$%^&*()_+'
    count = 0

    for char in li:
        if char in vowels:
            count += 1
            unique_li.append(str(char))

    print(f"Unique Elements from inserted string : {str1.join(unique_li)}")


def is_palindrome(digit_li):

    for i in digit_li:
        if len(str(i)) > 1:
            if str(i) == str(i)[::-1]:
                palindrome_li.append(str(i))

    print(f"Palindrom From Inserted String is : {str1.join(palindrome_li)}")


def is_square(digit_li):

    for i in digit_li:
        square_root = round(i**(1/2))
        if square_root * square_root == i:
            square_list.append(str(i))

    print(
        f"All The Square Numbers From Inserted String is : {str1.join(square_list)}")


def is_cube(digit_li):

    for i in digit_li:
        cube_root = round(i**(1/3))
        if cube_root * cube_root * cube_root == i:
            cube_list.append(str(i))

    print(
        f"All The Cube Numbers From Inserted String is : {str1.join(cube_list)}")


def is_match(li):

    for i in li:
        if len(i) > 1:
            if i[0] == i[-1]:
                same_latter.append(str(i))

    print(
        f"This Words/Numbers ends with The same latter/number fom the sting : {str1.join(same_latter)}")


def is_prime(digit_li):

    for i in digit_li:
        prime = sympy.isprime(i)
        if prime == True:
            prime_li.append(str(i))

    print(f"Prime Numbers in the entered string : {str1.join(prime_li)}")
