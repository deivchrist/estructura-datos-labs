test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class MinHeap:
    def __init__(self):
        # "We create an empty list to represent the heap"
        self.heap = []

    def is_empty(self):
        # "Returns True if the heap is empty"
        return len(self.heap) == 0

    def size(self):
        # "Returns the number of elements in the heap"
        return len(self.heap)

    def peek(self):
        # "Returns the minimum element without removing it, or None if the heap is empty"
        if self.is_empty():
            return None
        return self.heap[0]

def test_1_1():
    heap = MinHeap()
    record_test("1.1.1 Empty heap initialization", heap.is_empty() == True)
    
    heap.heap = [1, 3, 2]  # "We simulate already inserted elements"
    record_test("1.1.2 Size tracking", heap.size() == 3)
    
    record_test("1.1.3 Peek functionality", heap.peek() == 1)
    
    empty_heap = MinHeap()
    record_test("1.1.4 Empty heap edge case", empty_heap.peek() is None)
    
    record_test("1.1.5 Type validation", isinstance(heap.is_empty(), bool))

test_1_1()

for r in test_results:
    print(r)
