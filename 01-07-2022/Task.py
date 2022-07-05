def find_max_0_from_num(num):
    #     binary = bin(int(num))[2:]
    binary = '00000000000000100010000010011110'
    print(f"Binary of {int(num)} is {binary}")
    li = binary.split("1")
    max_0 = max(li)
    print(f"Max 0 from {int(num)}`s Binary is {max_0}")


def find_max_0_from_str(str1):
    bin_li = [bin(ord(i))[2:] for i in str1]
    print(f'Binary of {str1} is {"".join(bin_li)}')
    print(
        f'Max 0 from {str1}`s Binary is {len(max("".join(bin_li).split("1")))}')


n = input()

if n.isdigit():
    find_max_0_from_num(n)
else:
    find_max_0_from_str(n)
