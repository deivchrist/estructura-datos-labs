class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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

    def range_query(self, min_val, max_val):
        result = []

        def inorder(node):
            if not node:
                return
            if node.value > min_val:
                inorder(node.left)
            if min_val <= node.value <= max_val:
                result.append(node.value)
            if node.value < max_val:
                inorder(node.right)

        inorder(self.root)
        return result


def test_range_query():
    bst1 = BinarySearchTree()
    bst1.build_from_list([7, 3, 11, 1, 5, 9, 13])
    print("Test 1:", bst1.range_query(5, 10) == [5, 7, 9])

    bst2 = BinarySearchTree()
    bst2.build_from_list([6, 4, 8, 2])
    print("Test 2:", bst2.range_query(1, 10) == [2, 4, 6, 8])

    bst3 = BinarySearchTree()
    bst3.build_from_list([20, 10, 30])
    print("Test 3:", bst3.range_query(1, 5) == [])

    bst4 = BinarySearchTree()
    bst4.build_from_list([15])
    print("Test 4:", bst4.range_query(10, 20) == [15])

    bst5 = BinarySearchTree()
    bst5.build_from_list([15, 10, 20, 5, 25])
    print("Test 5:", bst5.range_query(10, 20) == [10, 15, 20])

# 🚀 Ejecutar pruebas
test_range_query()
