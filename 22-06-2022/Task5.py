# Task 5. Do calculation of sting and result it.

# String example: : 5, +, 10, -, 6, 5, *, 2, +, 3, 2, /, 4

# Answer is: : -17 [5 + 10 - 65 * 2 + 32 / 4]
from math import floor, trunc

string = "5, +, 1, 0, -, 6, 5, *, 2, +, 3, 2, /, 4"
s1 = string.split(",")
s2 = "".join(s1)
s3 = s2.replace(" ", "")
print(s3)


class Solution:
    def solve(self, s):
        s = list(s[::-1])

        def get_value():
            sign = 1
            if s and s[-1] == "-":
                s.pop()
                sign = -1
            value = 0
            while s and s[-1].isdigit():
                value *= 10
                value += int(s.pop())
            return sign * value

        def get_term():
            term = get_value()
            while s and s[-1] in "*/":
                op = s.pop()
                value = get_value()
                if op == "*":
                    term *= value
                else:
                    term = floor(1.0 * term / value)
            return term

        ans = get_term()
        while s:
            op, term = s.pop(), get_term()
            if op == "+":
                ans += term
            else:
                ans -= term
        return ans


ob = Solution()
print(ob.solve(s3))
