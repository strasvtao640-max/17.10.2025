import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))  # длина прыжка
    prev = 0

    # 1. Прыгаем вперёд блоками
    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # 2. Линейно ищем внутри блока
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i

    return -1


print(jump_search([1, 3, 5, 7, 9, 11, 15], 11))
