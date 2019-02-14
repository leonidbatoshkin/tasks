from functools import lru_cache

# @lru_cache(maxsize=None)
# def fib(n):
#     if n < 2:
#         return n
#     return fib(n-1) + fib(n-2)
#
# def main():
#     n = int(input())
#     print(fib(n))
#     print(fib.cache_info())
#
#
# if __name__ == "__main__":
#     main()

# n = int(input())
# a = int(str(n)[-1])
# b = int(str(n)[-2])
# if 0 <= a or b <= 9:
#     num = (a + b) % 10
#     print(num)

#########################################

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

def last_number(n) :
    return fib(n % 60) % 10

def main():
    n = int(input())
    print(last_number(n))


if __name__ == "__main__":
    main()