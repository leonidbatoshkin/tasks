# # Циклический сдвиг ВЛЕВО в массиве
# A = [1, 2, 3, 4, 5]  # A - массив и в нём N - элементов
# N = len(A)
# tmp = A[0]
# for k in range(N-1):
#     A[k] = A[k+1]
# A[N-1] = tmp
#
# for i in A:
#     print(i, end=" ")


# # Циклический сдвиг ВПРАВО в массиве
# A = [1, 2, 3, 4, 5]  # A - массив и в нём N - элементов
# N = len(A)
# tmp = A[N-1]
# for k in range(N-2, -1, -1):
#     A[k+1] = A[k]
# A[0] = tmp
#
# for i in A:
#     print(i, end=" ")


# Решето Эратосфена
N = int(input())
A = [True] * N
A[0] = A[1] = False
for k in range(2, N):
    if A[k]:
        for m in range(2*k, N, k):
            A[m] = False

for k in range(N):
    print(k, '-', "простое" if A[k] else "составное")