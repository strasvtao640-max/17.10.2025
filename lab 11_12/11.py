def permutations(s):
    # Базовый случай: если длина строки 0 или 1 — это единственная перестановка
    if len(s) <= 1:
        return [s]

    result = []  # список для всех перестановок

    # Перебираем каждый символ строки
    for i in range(len(s)):
        char = s[i]               # выбранный символ
        rest = s[:i] + s[i+1:]    # строка без этого символа

        # получаем перестановки остатка строки
        perms = permutations(rest)

        # добавляем символ в начало каждой перестановки
        for p in perms:
            result.append(char + p)

    return result


# ==== запуск программы ====
text = input("Введите строку: ")

all_perms = permutations(text)

print("Все перестановки:")
for p in all_perms:
    print(p)
