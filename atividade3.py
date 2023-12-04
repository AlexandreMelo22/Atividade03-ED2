# Importa o módulo time para medir o tempo de execução
import time

# Defini a classe Node para representar os nós da árvore
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

# Defini a classe AVLTree para representar a árvore AVL
class AVLTree:
    def __init__(self):
        self.root = None

    # Função para obter a altura de um nó
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    # Função para atualizar a altura de um nó
    def update_height(self, node):
        if not node:
            return 0
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        return node.height

    # Função para obter o fator de balanceamento de um nó
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # Função para realizar uma rotação à direita
    def rotate_right(self, y):
        x = y.left
        if not x:
            return y

        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    # Função para realizar uma rotação à esquerda
    def rotate_left(self, x):
        y = x.right
        if not y:
            return x

        T2 = y.left

        y.left = x
        x.right = T2

        self.update_height(x)
        self.update_height(y)

        return y

    # Função para inserir um novo nó na árvore
    def insert(self, key):
        self.root = self._insert(self.root, key)

    # Função auxiliar para inserir um novo nó na árvore
    def _insert(self, root, key):
        if not root:
            return Node(key)

        if key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)

        self.update_height(root)

        balance = self.get_balance(root)

        # Caso Left Left
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)

        # Caso Right Right
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)

        # Caso Left Right
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Caso Right Left
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    # Função para realizar uma travessia em ordem na árvore
    def inorder_traversal(self):
        self._inorder_traversal(self.root)
        print()

    # Função auxiliar para realizar uma travessia em ordem na árvore
    def _inorder_traversal(self, root):
        if root:
            self._inorder_traversal(root.left)
            print(root.key, end=" ")
            self._inorder_traversal(root.right)

# Teste com os dados fornecidos
numbers = [5371, 3724, -13805, 16190, 3945]

avl_tree = AVLTree()

start_time = time.time()

for num in numbers:
    avl_tree.insert(num)

end_time = time.time()

print("Árvore AVL em ordem:")
avl_tree.inorder_traversal()
print("Tempo para inserção na Árvore AVL: {} segundos".format(end_time - start_time))
