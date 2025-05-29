class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Inserta un valor en el árbol"""
        if not self.root:
            self.root = Node(value)
            return
        current = self.root
        while True:
            if value < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(value)
                    return
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(value)
                    return

    def build_from_list(self, values):
        """Construye el árbol desde una lista"""
        for v in values:
            self.insert(v)

    def kth_smallest(self, k):
        """📊 Encuentra el k-ésimo elemento más pequeño del BST"""
        self.counter = 0    # 📊 Contador de visitas
        self.result = None  # 🎯 Resultado final

        def inorder(node):
            if not node or self.result is not None:
                return
            inorder(node.left)  # ↙ Recorre subárbol izquierdo
            self.counter += 1   # 🧮 Visita nodo actual
            if self.counter == k:
                self.result = node.value  # 🎯 Encontrado
                return
            inorder(node.right)  # ↘ Recorre subárbol derecho

        inorder(self.root)
        return self.result


def test_kth_smallest():
    bst1 = BinarySearchTree()
    bst1.build_from_list([3, 1, 4, 2])
    print("🧪 Test 1:", bst1.kth_smallest(2) == 2)  # 🎯

    bst2 = BinarySearchTree()
    bst2.build_from_list([5, 3, 7, 2, 4, 6, 8])
    print("🧪 Test 2:", bst2.kth_smallest(1) == 2)  # 📉 Mínimo

    print("🧪 Test 3:", bst2.kth_smallest(7) == 8)  # 📈 Máximo

    bst3 = BinarySearchTree()
    bst3.build_from_list([4, 2, 6, 1, 3, 5, 7])
    print("🧪 Test 4:", bst3.kth_smallest(4) == 4)  # 🔗 Mitad

    bst4 = BinarySearchTree()
    bst4.build_from_list([10])
    print("🧪 Test 5:", bst4.kth_smallest(1) == 10)  # 🌱 Nodo único

# 🚀 Ejecutar todas las pruebas
test_kth_smallest()
