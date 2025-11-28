def power(x, n):
    # Базовый случай: если степень 0, то результат 1
    if n == 0:
        return 1

    # Если степень чётная
    if n % 2 == 0:
        half = power(x, n // 2)
        return half * half

    # Если степень нечётная
    return x * power(x, n - 1)

# Ввод данных от пользователя
x = float(input("Введите число x: "))
n = int(input("Введите степень n: "))

# Вызов функции и вывод результата
result = power(x, n)
print("Результат:", result)
