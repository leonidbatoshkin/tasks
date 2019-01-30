import itertools
import math


def primes():
    p = 1
    while True:  # просто пример
        p += 1
        if ((math.factorial(p - 1)) + 1) % p == 0:
            yield p



print(list(itertools.takewhile(lambda x : x <= 31, primes())))