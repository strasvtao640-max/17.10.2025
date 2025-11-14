def exponential_search(arr, target):
    if arr[0] == target:
        return 0

    i = 1

    # 1. Увеличиваем индекс экспоненциально
    while i < len(arr) and arr[i] <= target:
        i *= 2

    # 2. Бинарный поиск в нужном диапазоне
    left = i // 2
    right = min(i, len(arr) - 1)

    return binary_search(arr, target, left, right)


def binary_search(arr, target, left, right):
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


print(exponential_search([1,2,3,4,5,10,20,30], 10))
