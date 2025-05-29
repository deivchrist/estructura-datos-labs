class Node:
    def __init__(self, value):
        self.value = value
        self.left = None  # ⬅️ Anterior (prev)
        self.right = None # ➡️ Siguiente (next)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
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
        for v in values:
            self.insert(v)

    def bst_to_dll(self):
        """🔁 Convierte el BST a lista doblemente enlazada circular ordenada"""
        if not self.root:
            return None

        self.head = None  # 🎯 Inicio de la DLL
        self.prev = None  # 🔙 Nodo anterior al actual

        def inorder(node):
            if not node:
                return
            inorder(node.left)

            if self.prev:
                self.prev.right = node  # 🔗 prev ➡️ node
                node.left = self.prev   # 🔗 node ⬅️ prev
            else:
                self.head = node  # 🏁 Primer nodo visitado (mínimo)

            self.prev = node  # 🔄 Avanza el puntero prev

            inorder(node.right)

        inorder(self.root)

        # 🔄 Hacer la lista circular ⭕
        self.head.left = self.prev
        self.prev.right = self.head

        return self.head


# ✅ DLL validator helper
def validate_circular_dll(head, expected_values):
    if not head:
        return expected_values == []
    values = []
    current = head
    while True:
        values.append(current.value)
        current = current.right
        if current == head:
            break
    return values == expected_values

def test_bst_to_dll():
    bst1 = BinarySearchTree()
    bst1.build_from_list([2, 1, 3])
    head1 = bst1.bst_to_dll()
    print("🧪 Test 1:", validate_circular_dll(head1, [1, 2, 3]) == True)

    bst2 = BinarySearchTree()
    bst2.build_from_list([4, 2, 6, 1, 3, 5, 7])
    head2 = bst2.bst_to_dll()
    print("🧪 Test 2:", validate_circular_dll(head2, [1, 2, 3, 4, 5, 6, 7]) == True)

    bst3 = BinarySearchTree()
    bst3.build_from_list([5])
    head3 = bst3.bst_to_dll()
    print("🧪 Test 3:", validate_circular_dll(head3, [5]) == True)

    bst4 = BinarySearchTree()
    bst4.build_from_list([1, 2, 3, 4])
    head4 = bst4.bst_to_dll()
    print("🧪 Test 4:", validate_circular_dll(head4, [1, 2, 3, 4]) == True)

    bst5 = BinarySearchTree()
    head5 = bst5.bst_to_dll()
    print("🧪 Test 5:", head5 is None)

# 🚀 Ejecutar todas las pruebas
test_bst_to_dll()
