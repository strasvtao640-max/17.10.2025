def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # 1. Определяем минимальное и максимальное значения
    min_val, max_val = min(arr), max(arr)

    # 2. Создаём нужное количество корзин
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    # 3. Распределяем элементы по корзинам
    for num in arr:
        index = int((num - min_val) / (max_val - min_val + 1) * bucket_count)
        buckets[index].append(num)

    # 4. Сортируем каждую корзину
    for bucket in buckets:
        bucket.sort()

    # 5. Склеиваем корзины обратно
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr


# Пример
print(bucket_sort([0.2, 0.1, 0.4, 0.8, 0.3]))
