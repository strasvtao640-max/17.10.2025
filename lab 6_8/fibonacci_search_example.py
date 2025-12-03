def fibonacci_search(arr, x):
    n = len(arr)

    # создаём числа Фибоначчи
    fib_m2 = 0   # F(m-2)
    fib_m1 = 1   # F(m-1)
    fib_m = fib_m2 + fib_m1  # F(m)

    while fib_m < n:
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1

    offset = -1

    while fib_m > 1:
        i = min(offset + fib_m2, n - 1)

        if arr[i] < x:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i
        elif arr[i] > x:
            fib_m = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib_m - fib_m1
        else:
            return i

    if fib_m1 and offset + 1 < n and arr[offset + 1] == x:
        return offset + 1

    return -1


def main():
    arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
    x = 85
    idx = fibonacci_search(arr, x)

    print("Массив:", arr)
    print("Ищем элемент:", x)
    if idx != -1:
        print("Элемент найден на позиции (индекс):", idx)
    else:
        print("Элемент не найден")


if __name__ == "__main__":
    main()