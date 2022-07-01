# 2. Between the two BRTS stations Iscon and Riverfront,
#    there are 12 intermediate stations. Determine the number of ways a BRTS can be arranged to
#    stop at four of these intermediate stations so that no two stops are consecutive.

from math import factorial as fact


def find_station(n, r):
    t = (n - r) + 1
    return fact(t)//(fact(r)*(fact(t-r)))


find_station(12, 4)
