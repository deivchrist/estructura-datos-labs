class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Inserta un nodo en el BST"""
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
        """Crea el árbol a partir de una lista"""
        for v in values:
            self.insert(v)

    def is_valid_bst(self):
        """🧼 Verifica si el árbol cumple con las reglas del BST"""
        def validate(node, min_val, max_val):
            # Si el nodo es nulo, es válido (caso base)
            if not node:
                return True
            # El valor debe estar estrictamente entre min y max
            if not (min_val < node.value < max_val):
                return False
            # Validar recursivamente izquierda y derecha
            return (
                validate(node.left, min_val, node.value) and
                validate(node.right, node.value, max_val)
            )
        # Llamada inicial con rango infinito
        return validate(self.root, float('-inf'), float('inf'))

def test_is_valid_bst():
    bst1 = BinarySearchTree()
    bst1.build_from_list([5, 3, 7, 2, 4, 6, 8])
    print("🧪 Test 1:", bst1.is_valid_bst() == True)  # ✅ Árbol válido

    bst2 = BinarySearchTree()
    bst2.root = Node(5)
    bst2.root.left = Node(6)  # ❌ izquierda > root
    bst2.root.right = Node(7)
    print("🧪 Test 2:", bst2.is_valid_bst() == False)  # ❌ violación izquierda

    bst3 = BinarySearchTree()
    bst3.root = Node(5)
    bst3.root.left = Node(3)
    bst3.root.right = Node(4)  # ❌ derecha < root
    print("🧪 Test 3:", bst3.is_valid_bst() == False)  # ❌ violación derecha

    bst4 = BinarySearchTree()
    bst4.build_from_list([42])
    print("🧪 Test 4:", bst4.is_valid_bst() == True)  # 🌱 nodo único

    bst5 = BinarySearchTree()
    print("🧪 Test 5:", bst5.is_valid_bst() == True)  # 📭 árbol vacío

# 🚀 Ejecutar todas las pruebas
test_is_valid_bst()
