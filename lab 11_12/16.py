# Класс узла бинарного дерева
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Preorder: корень → левый → правый
def preorder(root):
    if root is None:
        return
    print(root.value, end=" ")
    preorder(root.left)
    preorder(root.right)


# Inorder: левый → корень → правый
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.value, end=" ")
    inorder(root.right)


# Postorder: левый → правый → корень
def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.value, end=" ")


# ======= Создаём дерево (пример) =======
#       1
#      / \
#     2   3
#    / \
#   4   5

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


# ======= Вывод всех обходов =======
print("Preorder:")
preorder(root)
print()

print("Inorder:")
inorder(root)
print()

print("Postorder:")
postorder(root)
print()
