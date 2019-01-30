# Алгоритм линейного поиска в массиве
def array_search(A: list, N: int, x: int):
    """Осуществляет поиск числа x в массиве A от 0 до N-1 индекса включительно.
        Возвращает индекс элемента x в массиве A.
        Или -1, если такого нет.
        Если в массиве несколько одинаковых элементов, равных x,
        то вернуть индекс первого по счёту.
    """
    for k in range(N):
        if A[k] == x:
            return k
    return -1

def test_array_search():
    A1 = [1, 2, 3, 4, 5]
    m = array_search(A1, 5, 8)
    if m == -1:
        print("#test1 - ok")
    else:
        print("#test1 - fail")

    A2 = [-1, -2, -3, -4, -5]
    m = array_search(A2, 5, -3)
    if m == 2:
        print("#test2 - ok")
    else:
        print("#test2 - fail")

    A3 = [10, 20, 30, 10, 10]
    m = array_search(A3, 5, 10)
    if m == 0:
        print("#test3 - ok")
    else:
        print("#test3 - fail")

test_array_search() # Запуск некой тестовой функции


# Алгоритм инвертирования массива
def invert_array(A:list, N:int):
    """ Обращение массива ( поворот задом-наперёд)
        в рамках индексов от 0 до N-1
    """
    for k in range(N//2):
        A[k], A[N-1-k] = A[N-1-k], A[k]


def test_invert_array():
    A1 = [1, 2, 3, 4, 5]
    print(A1)
    invert_array(A1, 5)
    print(A1)
    if A1 == [5, 4, 3, 2, 1]:
        print("#test1 - ok")
    else:
        print("#test1 - fail")

    A2 = [0, 0, 0, 0, 0, 0, 0, 10]
    print(A2)
    invert_array(A2, 8)
    print(A2)
    if A2 == [10, 0, 0, 0, 0, 0, 0, 0]:
        print("#test2 - ok")
    else:
        print("#test2 - fail")

test_invert_array()