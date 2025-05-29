class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Inserta un valor en el BST"""
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

    def find_lca(self, val1, val2):
        """🧬 Encuentra el Ancestro Común Más Bajo (LCA) de dos valores"""
        current = self.root
        while current:
            # Ambos valores están a la izquierda
            if val1 < current.value and val2 < current.value:
                current = current.left
            # Ambos valores están a la derecha
            elif val1 > current.value and val2 > current.value:
                current = current.right
            else:
                # Se bifurcan o uno es el nodo actual → LCA encontrado
                return current.value

def test_find_lca():
    bst1 = BinarySearchTree()
    bst1.build_from_list([6, 2, 8, 0, 4, 7, 9, 3, 5])
    print("🧪 Test 1:", bst1.find_lca(2, 8) == 6)  # 🌲 Root is LCA

    bst2 = BinarySearchTree()
    bst2.build_from_list([6, 2, 8, 0, 4, 7, 9, 3, 5])
    print("🧪 Test 2:", bst2.find_lca(0, 4) == 2)  # 📚 Subtree LCA

    bst3 = BinarySearchTree()
    bst3.build_from_list([6, 2, 8, 0, 4, 7, 9, 3, 5])
    print("🧪 Test 3:", bst3.find_lca(2, 3) == 2)  # 🔗 Ancestor node

    bst4 = BinarySearchTree()
    bst4.build_from_list([5, 3, 7])
    print("🧪 Test 4:", bst4.find_lca(5, 5) == 5)  # 🎯 Same node

    bst5 = BinarySearchTree()
    bst5.build_from_list([4, 2, 6, 1, 3, 5, 7])
    print("🧪 Test 5:", bst5.find_lca(1, 3) == 2)  # 🌿 Leaf node LCA

# 🚀 Ejecutar pruebas
test_find_lca()
