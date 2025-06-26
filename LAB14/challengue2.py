test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class MinHeap:
    def __init__(self):
        # "We create an empty list to represent the heap"
        self.heap = []
    
    def _parent_index(self, index):
        # Returns the index of the parent node, or None if index is 0 (the root)
        if index <= 0 or index >= len(self.heap):
            return None
        return (index - 1) // 2
    
    def _left_child_index(self, index):
        # Returns the index of the left child, but does not check if it exists
        return 2 * index + 1
    
    def _right_child_index(self, index):
        # Returns the index of the right child, but does not check if it exists
        return 2 * index + 2
    
    def _has_left_child(self, index):
       # Returns True if the computed index of the left child is within the range
        return self._left_child_index(index) < len(self.heap)
    
    def _has_right_child(self, index):
        # Returns True if the calculated index of the right child is within the range
        return self._right_child_index(index) < len(self.heap)

def test_1_2():
    # Create an example heap with 7 elements
    heap = MinHeap()
    heap.heap = [1, 3, 2, 7, 4, 5, 8]
    
    # 1.2.1 Parent calculation: The node at index 4 must have a parent at index 1
    record_test("1.2.1 Parent calculation", heap._parent_index(4) == 1)
    
# 1.2.2 Children calculation: node at index 1 must have children at 3 and 4
    left_correct = heap._left_child_index(1) == 3
    right_correct = heap._right_child_index(1) == 4
    record_test("1.2.2 Children calculation", left_correct and right_correct)
    
    # 1.2.3 Root node edge case: the root (index 0) has no parent
    root_parent = heap._parent_index(0)
    record_test("1.2.3 Root node edge case", root_parent == -1 or root_parent is None)
    
    # 1.2.4 Boundary validation: the node at index 1 must have both children
    has_children = heap._has_left_child(1) and heap._has_right_child(1)
    record_test("1.2.4 Boundary validation", has_children)
    
    # 1.2.5 Invalid index handling: the last node (index 6) has no children
    no_children = not heap._has_left_child(6) and not heap._has_right_child(6)
    record_test("1.2.5 Invalid index handling", no_children)

test_1_2()

for r in test_results:
    print(r)
