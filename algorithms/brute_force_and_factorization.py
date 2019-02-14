# Метод грубой силы
def is_simple_number(x):
    """Определяет является ли число простым
        Если простое - True, иначе False
        x - целое положительное число.
    """
    divisor = 2
    while divisor < x:
        if x % divisor == 0:
            return False
        divisor += 1
    return True

# Алгоритм разложения числа на множители (Алгоритм факторизации)
def factorize_number(x):
    """Раскладывает число на множители
        Печатает их на экран
        x - целое положительное число.
    """
    divisor = 2
    while x > 1:
        if x % divisor == 0:
            print(divisor)
            x //= divisor
        else:
            divisor += 1

factorize_number(0)