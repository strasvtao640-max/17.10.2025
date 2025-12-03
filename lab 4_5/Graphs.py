from collections import deque

# Собственное представление общего дерева (каждый узел может иметь много детей)
class TreeNode:
    def __init__(self, value: str) -> None:
        self.value = value
        self.children: list["TreeNode"] = []

    def add_child(self, child: "TreeNode") -> None:
        self.children.append(child)


def print_tree(root: TreeNode, level: int = 0) -> None:
    indent = "  " * level
    print(f"{indent}{root.value}")
    for child in root.children:
        print_tree(child, level + 1)


# Собственное представление неориентированного графа через список смежности
class Graph:
    def __init__(self) -> None:
        self.adj: dict[str, list[str]] = {}

    def add_vertex(self, v: str) -> None:
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, v1: str, v2: str) -> None:
        # добавляем вершины, если их ещё нет
        self.add_vertex(v1)
        self.add_vertex(v2)
        # так как граф неориентированный, добавляем ребро в обе стороны
        self.adj[v1].append(v2)
        self.adj[v2].append(v1)

    def bfs(self, start: str) -> list[str]:
        """Простой обход в ширину от вершины start."""
        if start not in self.adj:
            return []
        visited: set[str] = {start}
        queue: deque[str] = deque([start])
        order: list[str] = []
        while queue:
            v = queue.popleft()
            order.append(v)
            for neighbor in self.adj[v]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order


if __name__ == "__main__":
    # -------- Пример дерева: структура категорий интернет-магазина --------
    root = TreeNode("Все категории")
    electronics = TreeNode("Электроника")
    clothes = TreeNode("Одежда")
    home = TreeNode("Товары для дома")

    root.add_child(electronics)
    root.add_child(clothes)
    root.add_child(home)

    phones = TreeNode("Смартфоны")
    laptops = TreeNode("Ноутбуки")
    electronics.add_child(phones)
    electronics.add_child(laptops)

    print("Структура категорий (дерево):")
    print_tree(root)

    # -------- Пример графа: сеть городов и дорог между ними --------
    g = Graph()
    g.add_edge("Москва", "Тула")
    g.add_edge("Москва", "Казань")
    g.add_edge("Тула", "Воронеж")
    g.add_edge("Казань", "Нижний Новгород")
    g.add_edge("Воронеж", "Ростов-на-Дону")

    print("\nОбход графа дорог из города 'Москва':")
    print(g.bfs("Москва"))