def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def main():
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Исходный массив:", arr)
    bubble_sort(arr)
    print("Отсортированный массив (пузырьком):", arr)


if __name__ == "__main__":
    main()
