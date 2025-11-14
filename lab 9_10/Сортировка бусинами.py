def bead_sort(arr):
    if any(x < 0 for x in arr):
        raise ValueError("Bead sort works only with positive integers.")

    max_num = max(arr)

    # 1. Создаём матрицу из "бусин"
    beads = [[0] * max_num for _ in arr]

    # 2. Заполняем бусинами каждую строку
    for i, num in enumerate(arr):
        for j in range(num):
            beads[i][j] = 1

    # 3. «Падаем вниз» — считаем 1 в каждом столбце
    for j in range(max_num):
        count = sum(beads[i][j] for i in range(len(arr)))
        for i in range(len(arr)):
            beads[i][j] = 1 if i >= len(arr) - count else 0

    # 4. Переводим обратно в числа
    sorted_arr = [sum(row) for row in beads]
    return sorted_arr


print(bead_sort([5, 3, 1, 7, 4]))
