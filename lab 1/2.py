def split_numbers(numbers):
    # Используем списковые включения для фильтрации чисел
    first_group = [num for num in numbers if num <= 5]
    second_group = [num for num in numbers if num > 5]
    
    return first_group, second_group

def split_numbers_with_reverse(numbers):
    # Альтернативный вариант с явным обратным порядком
    first_group = [num for num in numbers if num <= 5][::-1]
    second_group = [num for num in numbers if num > 5][::-1]
    
    return first_group, second_group

# Исходный массив цифр от 1 до 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Исходный массив:", numbers)

# Разбиваем числа на два списка
list1, list2 = split_numbers(numbers)

# Выводим результаты
print("Первый список (1-5):", list1)
print("Второй список (6-10):", list2)

# Демонстрация с обратным порядком (как в оригинале)
list1_rev, list2_rev = split_numbers_with_reverse(numbers)
print("\nС обратным порядком (LIFO):")
print("Первый список (1-5):", list1_rev)
print("Второй список (6-10):", list2_rev)

# Дополнительная информация
print(f"\nСтатистика:")
print(f"В первом списке: {len(list1)} чисел")
print(f"Во втором списке: {len(list2)} чисел")
