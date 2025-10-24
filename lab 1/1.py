def is_number_palindrome(number):
    # Преобразуем число в строку
    num_str = str(number)
    
    # Используем срезы для сравнения строки с её обратной версией
    return num_str == num_str[::-1]


# Получаем ввод от пользователя
try:
    number = int(input("Введите положительное число: "))
    
    if number < 0:
        print("Ошибка: введите положительное число!")
    else:
        # Проверяем и выводим результат
        if is_number_palindrome(number):
            print(f"Число {number} является палиндромом!")
        else:
            print(f"Число {number} НЕ является палиндромом!")
            
except ValueError:
    print("Ошибка: введите целое число!")
