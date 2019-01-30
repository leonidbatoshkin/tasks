from random import randint
# Бинарный поиск в массиве
def compare(left_bound:int, right_bound:int):
    if right_bound - left_bound == 1:
        return -1
    return left_bound + 1


def left_bound(sequence, key):
    left = -1
    right = len(sequence)
    while right - left > 1:
        middle = (left + right) // 2
        if sequence[middle] < key:
            left = middle
        else:
            right = middle
    return left

def right_bound(sequence, key):
    left = -1
    right = len(sequence)
    while right - left > 1:
        middle = (left + right) // 2
        if sequence[middle] <= key:
            left = middle
        else:
            right = middle
    return right


def binary_search(A, key):
    return compare(left_bound(A, key), right_bound(A, key))

mas = sorted([randint(0, 10) for x in range(11)])
print(mas)
print(binary_search(mas, 6))

