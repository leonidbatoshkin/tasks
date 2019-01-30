# Быстрое число Фибонначи через сохранение значений в список
n = int(input())
fib = [0, 1] + [0] * (n - 1)
for i in range(2, n + 1):
    fib[i] = fib[i-1] + fib[i-2]


# Количество возможных траекторий из 1 в N с запретом некоторых точек
def count_trajectories(N, allowed:list):
    K = [0, 1, int(allowed[2])] + [0] * (N-3)
    for i in range(3, N + 1):
        if allowed[i]:
            K[i] = K[i - 1] + K[i - 2] + K[i - 3]


# Минимальная стоимость достижения позиции N
def count_min_cost(N, price:list):
    C = [float("-inf"), price[0], price[1], price[1] + price[2]] + [0] * (N - 2)
    for i in range(3, N + 1):
        C[i] = price[1] + price[min(C[i - 1], C[i - 2])]
    return C[N]