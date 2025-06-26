test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class MinHeap:
    def __init__(self):
        # "we create an empty list to represent the heap"
        self.heap = []
    
    def insert(self, value):
        # "We add the new value to the end of the heap"
        self.heap.append(value)
        # "We apply heapify up from that index"
        self._heapify_up(len(self.heap) - 1)
    
    def _heapify_up(self, index):
        # We calculate the parent index
        
        parent = self._parent_index(index)
        # As long as the index is not root and the current value is less than its parent
        while index > 0 and self.heap[index] < self.heap[parent]:
            # We exchange the value with its father
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = self._parent_index(index)
    
    def _parent_index(self, index):
       # Returns the index of the parent, or -1 if it is root
        return (index - 1) // 2 if index > 0 else -1
    
    def size(self):
       # Returns the number of elements in the heap
        return len(self.heap)
    
    def peek(self):
       #Returns the minimum without removing it
        return self.heap[0] if self.heap else None

def test_1_3():
    heap = MinHeap()
    
    # 1.3.1 Single element insertion – insertar en heap vacío
    heap.insert(5)
    record_test("1.3.1 Single element insertion", heap.heap == [5])
    
   # 1.3.2 Multiple insertions – add multiple and validate size
    heap.insert(3)
    heap.insert(8)
    heap.insert(1)
    record_test("1.3.2 Multiple insertions", len(heap.heap) == 4)
    
    # 1.3.3 Minimum tracking – the minimum always at the root
    record_test("1.3.3 Minimum tracking", heap.peek() == 1)
    
    # 1.3.4 Heap property validation – padre <= hijos en todo el heap
    valid_heap = all(
        heap.heap[i] <= heap.heap[2*i+1] if 2*i+1 < len(heap.heap) else True
        for i in range(len(heap.heap)//2)
    )
    record_test("1.3.4 Heap property validation", valid_heap)
    
    # 1.3.5 Size consistency –the heap must have 4 elements
    record_test("1.3.5 Size consistency", heap.size() == 4)


test_1_3()

for r in test_results:
    print(r)
