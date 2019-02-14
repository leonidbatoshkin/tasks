# Сортировка слиянием
# Слияние массивов
def merge(A:list, B:list):
    C = [0] * (len(A) + len(B))
    i = k = n = 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
            n += 1
        else:
            C[n] = B[k]
            k += 1
            n += 1
    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1
    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1
    return C


# Сортировка
def merge_sort(A):
    if len(A) <= 1:
        return
    middle = len(A) // 2
    L = [A[i] for i in range(middle)]
    R = [A[i] for i in range(middle, len(A))]
    merge_sort(L)
    merge_sort(R)
    C = merge(L, R)
    for i in range(len(A)):
        A[i] = C[i]
    return A

# print(merge_sort([4, 2, 5, 3, 6, 1]))

# Сортировка Хоара
def hoar_sort(A:list):
    if len(A) <= 1:
        return
    barrier = A[0]
    L, M, R = [], [], []
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
    hoar_sort(L)
    hoar_sort(R)
    k = 0
    for x in L + M + R:
        A[k] = x
        k += 1
    return A

# print(hoar_sort([4, 2, 5, 3, 6, 1]))


# Проверка упорядоченности массива
def check_sorted(A, ascending=True):
    """Провекрка отсортированности массива за O(len(A))
        ascending - булевая переменная для того чтобы при вызове функции можно было уточнить
        проверять ли массив на отсортированность по убыванию(False) или по возрастанию(True)
    """
    flag = True
    s = 2 * int(ascending) - 1
    for i in range(len(A) - 1):
        if s * A[i] > s * A[i+1]:
            flag = False
            break
    return flag

ss = hoar_sort([4, 2, 5, 3, 6, 1])[::-1]
print(check_sorted(ss, False))
