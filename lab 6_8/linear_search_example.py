def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1


def main():
    arr = [3, 5, 2, 7, 9, 1, 4]
    target = 7
    index = linear_search(arr, target)

    print("Массив:", arr)
    print("Ищем элемент:", target)

    if index != -1:
        print(f"Элемент найден на позиции (индекс): {index}")
    else:
        print("Элемент не найден")


if __name__ == "__main__":
    main()
