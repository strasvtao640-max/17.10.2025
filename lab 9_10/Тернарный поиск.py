def ternary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        # 1. Делим отрезок на 3 части
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        # 2. Проверяем оба mid
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2

        # 3. Определяем, куда идти
        if target < arr[mid1]:
            right = mid1 - 1
        elif target > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1

    return -1


print(ternary_search([1,2,3,4,5,6,7,8], 6))
