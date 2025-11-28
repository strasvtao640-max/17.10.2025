# Лабиринт 5x5
maze = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# отмечаем посещенные клетки
visited = [[False]*5 for _ in range(5)]

def ok(x, y):
    return x >= 0 and x < 5 and y >= 0 and y < 5 and maze[x][y] == 0

# рекурсивный поиск
def find_paths(x, y):
    # если дошли до конца — возвращаем 1 путь
    if x == 4 and y == 4:
        return 1

    visited[x][y] = True
    total = 0

    # вниз
    if ok(x+1, y) and not visited[x+1][y]:
        total += find_paths(x+1, y)

    # вверх
    if ok(x-1, y) and not visited[x-1][y]:
        total += find_paths(x-1, y)

    # вправо
    if ok(x, y+1) and not visited[x][y+1]:
        total += find_paths(x, y+1)

    # влево
    if ok(x, y-1) and not visited[x][y-1]:
        total += find_paths(x, y-1)

    visited[x][y] = False
    return total


# запускаем
count = find_paths(0, 0)
print("Всего путей:", count)