def reverse_string(s):
    # Базовый случай: если строка пустая или длина 1 — просто возвращаем её
    if len(s) <= 1:
        return s

    # Рекурсивный шаг: берём последний символ + переворачиваем остальное
    return s[-1] + reverse_string(s[:-1])


# ==== запуск программы ====
text = input("Введите строку: ")
result = reverse_string(text)
print("Перевёрнутая строка:", result)