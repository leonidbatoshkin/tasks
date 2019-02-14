import graphics as gr

window = gr.GraphWin("Russian game", 600, 600)
alpha = 0.2
def fractal_rectangle(A, B, C, D, deep=10):
    if deep < 1:
        return
    # gr.Line(gr.Point(*A), gr.Point(*B)).draw(window)
    # gr.Line(gr.Point(*B), gr.Point(*C)).draw(window)
    # gr.Line(gr.Point(*C), gr.Point(*D)).draw(window)
    # gr.Line(gr.Point(*D), gr.Point(*A)).draw(window)
    for M, N in (A, B), (B, C), (C, D), (D, A):
        gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)
    A1 = (A[0] * (1 - alpha) + B[0] * alpha, A[1] * (1 - alpha) + B[1] * alpha)
    B1 = (B[0] * (1 - alpha) + C[0] * alpha, B[1] * (1 - alpha) + C[1] * alpha)
    C1 = (C[0] * (1 - alpha) + D[0] * alpha, C[1] * (1 - alpha) + D[1] * alpha)
    D1 = (D[0] * (1 - alpha) + A[0] * alpha, D[1] * (1 - alpha) + A[1] * alpha)
    fractal_rectangle(A1, B1, C1, D1, deep-1)
    window.getMouse()


fractal_rectangle((100, 100), (500, 100), (500, 500), (100, 500))

# Алгоритм Евклида
def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a-b, b)
    else:  # a < b
        return gcd(a, b-a)


# Улучшенный алгоритм Евклида
def better_gcd(a, b):
    if b == 0:
        return a
    else:
        return better_gcd(b, a % b)


# Быстрый Евклид в две строки
def the_best_gcd(a, b):
    return a if b == 0 else better_gcd(b, a % b)


print(gcd(12, 36))
print(the_best_gcd(12, 36))


# Возведение в степень
def pow(a: float, n: int):
    return 1 if n == 0 else pow(a, n-1) * a


# Логарифмически быстрое возведение в степень
def sup_pow(a: float, n: int):
    if n == 0:
        return 1
    elif n % 2 == 1:  # n - нечётное
        return sup_pow(a, n-1) * a
    else:  # n - чётное
        return sup_pow(a ** 2, n // 2)


print(sup_pow(2, 100))

# Ханойские башни
def move(n, start, finish):
    if n == 1:
        print(n, start, finish)
    else:
        tmp = 6 - start - finish
        move(n-1, start, tmp)
        print(n, start, finish)
        move(n-1, tmp, finish)